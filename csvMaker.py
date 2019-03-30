import csv
from datetime import datetime
import requests

with open('ASC 2018 Segment 1_truncated.txt', 'r') as f:
  reader = csv.reader(f)
  segment = list(reader)

coordinates = [i[2:4] for i in segment[1::2]]
URL = 'https://api.darksky.net/forecast/9ee4a75602f09db95f5b1eeee3fa2910/' + coordinates[0][0] + ',' + coordinates[0][1]
exclude = 'currently,minutely,daily,alerts,flags'
PARAMS = {'exclude':exclude}
r = requests.get(url = URL, params = PARAMS).json()
cloudCover = [[None]*(len(r['hourly']['data'])+2) for i in range(len(coordinates))]
time = [None]*(len(r['hourly']['data'])+2)
time[0:2] = ['Latitude','Longitude']
for i, data in enumerate(r['hourly']['data']):
    time[i+2] = datetime.utcfromtimestamp(data['time']).strftime("%m/%d/%Y, %H:%M:%S")

for i, [lat,lon] in enumerate(coordinates):
    cloudCover[i][0:2] = [lat,lon]
    URL = 'https://api.darksky.net/forecast/9ee4a75602f09db95f5b1eeee3fa2910/' + lat + ',' + lon
    r = requests.get(url = URL, params = PARAMS).json()
    for j, data in enumerate(r['hourly']['data']):
        cloudCover[i][j+2] = data['cloudCover']
        
with open('darkskytest.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(time)
    writer.writerows(cloudCover)
    print('CSV written!')

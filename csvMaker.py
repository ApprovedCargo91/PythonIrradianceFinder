import csv
from datetime import datetime
import requests

# File to extract coordinates from
filename = 'ASC 2018 Segment 1_truncated'

# API key stored locally in text file
with open('APIKey.txt','r') as f:
    key = f.readline().rsplit()[0]

# Get a two-dimensional list from race data
with open(filename + '.txt', 'r') as f:
    reader = csv.reader(f)
    segment = list(reader)

# Make a request to extract time data
coordinates = [i[2:4] for i in segment[1::2]]
URL = 'https://api.darksky.net/forecast/' + key + '/' + coordinates[0][0] + ',' + coordinates[0][1]
exclude = 'currently,minutely,daily,alerts,flags'
PARAMS = {'exclude':exclude}
r = requests.get(url = URL, params = PARAMS).json()
print('Connection made! Extracting data...')
# Initialize lists for cloud cover and time data
cloudCover = [[None]*(len(r['hourly']['data'])+2) for i in range(len(coordinates))]
time = [None]*(len(r['hourly']['data'])+2)
time[0:2] = ['Latitude','Longitude']
# Write sampled times to the time list
for i, data in enumerate(r['hourly']['data']):
    time[i+2] = datetime.utcfromtimestamp(data['time']).strftime("%m/%d/%Y, %H:%M:%S")
# Make a request for every lat and lon in coordinates, then write to cloudCover
for i, [lat,lon] in enumerate(coordinates):
    cloudCover[i][0:2] = [lat,lon]
    URL = 'https://api.darksky.net/forecast/9ee4a75602f09db95f5b1eeee3fa2910/' + lat + ',' + lon
    r = requests.get(url = URL, params = PARAMS).json()
    for j, data in enumerate(r['hourly']['data']):
        cloudCover[i][j+2] = data['cloudCover']

# Write time and cloud cover data to CSV file
with open(filename + '.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(time)
    writer.writerows(cloudCover)
    print('CSV written!')

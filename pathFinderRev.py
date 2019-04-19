import csv
import sys
import matplotlib.pyplot as plt

plt.ion()

filename = 'darkskytest'
# Get cloud cover data from CSV file
with open(filename + '.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

strs = [i[2:] for i in data[1:]]
cloudCover = [list(map(float, i)) for i in strs]
lx, lt = len(cloudCover), len(cloudCover[0])
t = list(range(0, lt))
tmp = [i - 0.5 for i in range(1, lt)]
v = [0]*(lt - 1)
x = [0]*(lt)
distRem = lx
currTime = 0
topSpeed = 8
while distRem > topSpeed:
    v[currTime] = topSpeed
    x[currTime + 1] = x[currTime] + topSpeed
    distRem -= topSpeed
    currTime += 1
    if distRem > 0 and currTime == lt - 1:
        print("Your top speed is too slow!")
        sys.exit()
if distRem > 0:
    v[currTime] = distRem/topSpeed
    x[currTime + 1] = x[currTime] + distRem
    currTime += 2
while currTime < lt:
    x[currTime] = x[currTime - 1]
    currTime += 1
plt.plot(t, x)
plt.plot(tmp, v)
plt.xlim(left=-0.1)
plt.ylim(bottom=-0.1)

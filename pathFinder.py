import csv
import sys

filename = 'darkskytest'
# Get cloud cover data from CSV file
with open(filename + '.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

strs = [i[2:] for i in data[1:]]
cloudCover = [list(map(float, i)) for i in strs]
# Determine the maximum and minimum speed
highSpeed = 20
lowSpeed = 10
speedRange = highSpeed - lowSpeed
lx, lt = len(cloudCover), len(cloudCover[0])
# Initialize two-dimensional list of paths and list of cloud cover sums
paths = [[None]*(lx+1) for i in range(speedRange)]
pathsENet = [None]*speedRange
startPoint = cloudCover[0][0]

# Finding all straight line paths with constant speed between highSpeed and lowSpeed
for deltaX in range(highSpeed, lowSpeed, -1):
    distRem = lx - deltaX
    currTime = 0
    while distRem > 0:
        paths[deltaX - speedRange - 1][currTime] = cloudCover[deltaX*(currTime+1)][currTime]
        currTime += 1
        distRem -= deltaX
        if currTime >= 49:
            print("Your inputted low speed is too slow!")
            sys.exit()
    if distRem < 0:
        finalPoint = cloudCover[lx-1][currTime]
        paths[deltaX - speedRange - 1][currTime] = finalPoint*abs(distRem/deltaX)

# Iterating through each generated path
for i, path in enumerate(paths):
    j = 0
    ccSum = startPoint
    while (j < lx) and (path[j] != None):
        ccSum += path[j]
        j += 1
    ccSum *= (i+1)
    pathsENet[i] = ccSum

# A sum of all the cloud cover values along any given straight line path
print(pathsENet)

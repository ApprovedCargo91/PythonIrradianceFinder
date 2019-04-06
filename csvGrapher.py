import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

filename = 'darkskytest'

# Turn on interactive mode, required to display on Mac
plt.ion()

# Read CSV into two-dimensional list
with open(filename + '.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Extract cloud cover data and convert to floats
strs = [i[2:] for i in data[1:]]
cloudCover = [list(map(float, i)) for i in strs]
# Create meshgrid of time and distance
lx, lt = len(cloudCover), len(cloudCover[0])
x, t = range(0, lx), range(0, lt)
xi, ti = np.meshgrid(x, t)

# Initialize and display figure
fig = plt.figure()
plt.imshow(cloudCover, vmin = np.amin(cloudCover), vmax=np.amax(cloudCover))
plt.xlabel('Time (hours)')
plt.ylabel('Distance')
plt.yticks([0,lx-1], ['Start','End'])
plt.colorbar()
plt.set_cmap('jet')
# Make 0 on y-axis meet 0 on x-axis
plt.gca().invert_yaxis()

import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

plt.ion()

with open('darkskytest.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

strs = [i[2:] for i in data[1:]]
cloudCover = [list(map(float, i)) for i in strs]
lx, lt = len(cloudCover), len(cloudCover[0])
x, t = range(0, lx), range(0, lt)
xi, ti = np.meshgrid(x, t)
grad = np.gradient(cloudCover)
mag = np.sqrt(grad[0]**2 + grad[1]**2)

fig = plt.figure()
rbf = scipy.interpolate.Rbf(xi, ti, cloudCover)
plt.imshow(cloudCover, vmin = np.amin(cloudCover), vmax=np.amax(cloudCover))
plt.xlabel('Time (hours)')
plt.ylabel('Distance')
plt.yticks([0,lx-1], ['Start','End'])
plt.colorbar()
plt.gca().invert_yaxis()

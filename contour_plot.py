import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
X, Y = np.mgrid[-1:1:60j, -1:1:30j]

#function
Z = np.sin(np.pi*X)*np.sin(np.pi*Y)

# plot surface
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.plot_surface(X, Y, Z, cmap="autumn_r", lw=0.5, rstride=1, cstride=1)

# 14 is contour plot 
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.contourf(X, Y, Z, zdir='z', offset=-0.5,cmap='cool')

#ax.plot(xs, ys, np.full_like(xs, -0.5))




#ax.contour(X, Y, Z, 10, lw=3, cmap="autumn_r", linestyles="solid", offset=-1)
plt.show()

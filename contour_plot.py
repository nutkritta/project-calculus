"""
# importing libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
# defining surface and axes
x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
y = x.copy().T
z = np.cos(x ** 2 + y ** 3)
 
fig = plt.figure()
 
# syntax for 3-D plotting
ax = plt.axes(projection ='3d')
 
# syntax for plotting
ax.plot_surface(x, y, z, cmap ='viridis', edgecolor ='green')
ax.set_title('Surface plot geeks for geeks')
plt.show()
"""
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(20,20))
x1 = np.arange(-1,1,0.1)
y1 = np.arange(-1,1,0.1)
x2 = np.arange(-2,-0.9,0.1)
y2 = np.arange(-1,1,0.1)
X1,Y1 = np.meshgrid(x1,y1)
X2,Y2 = np.meshgrid(x2,y2)

#function
Z1 = np.sin(np.pi*X1)*np.sin(np.pi*Y1)
Z2 = X2**2-Y2**2-1

# plot surface
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.plot_surface(X1, Y1, Z1, cmap="autumn_r", lw=0.5, rstride=1, cstride=1)
ax.plot_surface(X2, Y2, Z2, cmap="gray", lw=0.5, rstride=1, cstride=1)

# 14 is contour plot 
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.contourf(X1, Y1, Z1, zdir='z', offset=0.0,cmap='autumn_r')
ax.contourf(X2, Y2, Z2, zdir='z', offset=0.0,cmap='gray')

#ax.plot(xs, ys, np.full_like(xs, -0.5))

#ax.contour(X, Y, Z, 10, lw=3, cmap="autumn_r", linestyles="solid", offset=-1)


plt.show()
x = 0:0.001:10
y1 = x.^3;
y2 = 3.^x;

plot(x, y1);
hold on; % without this one will delete y1 before drawing y2
plot(x, y2, 'r');




"""import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
X, Y = np.mgrid[-1:1:60j, -1:1:30j]


#function
Z1 = np.sin(np.pi*X)*np.sin(np.pi*Y)
Z2 = X**2-Y**2-1

# plot surface
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.plot_surface(X, Y, Z1, cmap="autumn_r", lw=0.5, rstride=1, cstride=1)
ax.plot_surface(X, Y, Z2, cmap="gray", lw=0.5, rstride=1, cstride=1)

# 14 is contour plot 
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.contourf(X, Y, Z1, zdir='z', offset=-0.5,cmap='cool')
ax.contourf(X, Y, Z2, zdir='z', offset=-0.5,cmap='gray')

#ax.plot(xs, ys, np.full_like(xs, -0.5))




#ax.contour(X, Y, Z, 10, lw=3, cmap="autumn_r", linestyles="solid", offset=-1)

from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-6, 6, 0.3)
Y = np.arange(-6, 6, 0.3)
X, Y = np.meshgrid(X, Y)
Z = np.sin(X**2 + Y**2) / (X**2 + Y**2)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=1, antialiased=True)

# Customize the z axis
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.4, aspect=5)

plt.title("3D Graph")
ax.set_ylabel('y values', fontsize=8)
ax.set_xlabel('x values', fontsize=8)
ax.set_zlabel('z values', fontsize=8)

plt.show()

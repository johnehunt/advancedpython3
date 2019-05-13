from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt
from matplotlib import cm
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

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.4, aspect=5)

# Add labels to the graph
plt.title("3D Graph")
ax.set_ylabel('y values', fontsize=8)
ax.set_xlabel('x values', fontsize=8)
ax.set_zlabel('z values', fontsize=8)

plt.show()

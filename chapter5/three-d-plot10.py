from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as pyplot
from matplotlib import cm
import numpy as np

figure = pyplot.figure()
ax = figure.gca(projection='3d')

# Make data.
x_values = np.arange(-6, 6, 0.3)
y_values = np.arange(-6, 6, 0.3)
x_values, y_values = np.meshgrid(x_values, y_values)
z_values = np.sin(x_values ** 2 + y_values ** 2) / (x_values ** 2 + y_values ** 2)

# Plot the surface.
surf = ax.plot_surface(x_values,
                       y_values,
                       z_values,
                       cmap=cm.coolwarm,
                       linewidth=1,
                       antialiased=True)

# Add a color bar which maps values to colors.
figure.colorbar(surf, shrink=0.4, aspect=5)

# Add labels to the graph
pyplot.title("3D Graph")
ax.set_ylabel('y values', fontsize=8)
ax.set_xlabel('x values', fontsize=8)
ax.set_zlabel('z values', fontsize=8)

pyplot.show()

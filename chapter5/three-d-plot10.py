import matplotlib.pyplot as pyplot
# Import matplotlib colour map
from matplotlib import cm as colourmap
# Required for £D Projections
from mpl_toolkits.mplot3d import Axes3D
# Provide access to numpy functions
import numpy as np

# Make the data to be displayed
x_values = np.arange(-6, 6, 0.3)
y_values = np.arange(-6, 6, 0.3)

# Generate coordinate matrices from coordinate vectors
x_values, y_values = np.meshgrid(x_values, y_values)

# Generate Z values as sin of x plus y values
z_values = np.sin(x_values + y_values)

# Obtain the figure object
figure = pyplot.figure()

# Get the axes object for the 3D graph
axes = figure.gca(projection='3d')

# Plot the surface.
surf = axes.plot_surface(x_values,
                         y_values,
                         z_values,
                         cmap=colourmap.coolwarm)

# Add a color bar which maps values to colors.
figure.colorbar(surf)

# Add labels to the graph
pyplot.title("3D Graph")
axes.set_ylabel('y values', fontsize=8)
axes.set_xlabel('x values', fontsize=8)
axes.set_zlabel('z values', fontsize=8)

# Display the graph
pyplot.show()

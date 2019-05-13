import matplotlib.pyplot as pyplot
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# Initialize a Figure
figure = pyplot.figure()

# Add Axes to the Figure
axis = figure.add_subplot(111)
axis.plot(t, s, color='green', label='yyy')
axis.set(xlabel='time (s)', ylabel='voltage (mV)', title='Simple Plot')

x = 2.25 * np.random.rand(10)
y = 2.25 * np.random.rand(10)
axis.scatter(x, y, marker='o', label='xxx')

# Show the grid
axis.grid(linestyle='dashed')

# Display the Legend
axis.legend()

# Generate the plot
pyplot.show()


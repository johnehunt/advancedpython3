import matplotlib.pyplot as pyplot

t = range(0, 20)
s = range(30, 10, -1)
# Set up the grid of subplots to be 2 by 2
grid_size='22'

# Initialize a Figure
figure = pyplot.figure()

# Add first subplot
position = grid_size + '1'
print('Adding first subplot to position', position)
axis1 = figure.add_subplot(position)
axis1.set(title='subplot(2,2,1)')
axis1.plot(t, s)

# Add second subplot
position = grid_size + '2'
print('Adding second subplot to position', position)
axis2 = figure.add_subplot(position)
axis2.set(title='subplot(2,2,2)')
axis2.plot(t, s, 'r-')

# Add third subplot
position = grid_size + '3'
print('Adding third subplot to position', position)
axis3 = figure.add_subplot(position)
axis3.set(title='subplot(2,2,3)')
axis3.plot(t, s, 'g-')

# Add fourth subplot
position = grid_size + '4'
print('Adding fourth subplot to position', position)
axis4 = figure.add_subplot(position)
axis4.set(title='subplot(2,2,4)')
axis4.plot(t, s, 'y-')

# Display the chart
pyplot.show()

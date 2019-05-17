import matplotlib.pyplot as pyplot

t = range(0, 20)
s = range(30, 10, -1)

# Initialize a Figure
figure = pyplot.figure()

# Add first subplot
axis1 = figure.add_subplot(2, 2, 1)
axis1.set(title='subplot(2,2,1)')
axis1.plot(t, s)

# Add second subplot
axis2 = figure.add_subplot(2, 2, 2)
axis2.set(title='subplot(2, 2, 2')
axis2.plot(t, s, 'r-')

# Add third subplot
axis3 = figure.add_subplot(2, 2, 3)
axis3.set(title='subplot(2, 2, 3')
axis3.plot(t, s, 'g-')

# Add fourth subplot
axis4 = figure.add_subplot(2, 2, 4)
axis4.set(title='subplot(2, 2, 4')
axis4.plot(t, s, 'y-')

# Display the chart
pyplot.show()

import matplotlib.pyplot as pyplot

# Set up the data
labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5)
sizes = [45, 10, 15, 30, 22]

# Set up the multi-coloured bar chart
pyplot.bar(index, sizes, tick_label=labels, color=('red', 'green', 'blue', 'yellow', 'orange'))

# Configure the layout
pyplot.ylabel('Usage')
pyplot.xlabel('Programming Languages')

# Display the chart
pyplot.show()

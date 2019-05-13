# Pie chart, where the slices will be ordered and plotted counter-clockwise:

import matplotlib.pyplot as pyplot

labels = 'Python', 'Scala', 'C#', 'Java'
sizes = [45, 10, 15, 30]

# only "explode" the 3rd slice (i.e. 'Python')
explode = (0.1, 0, 0, 0)

fig1, ax1 = pyplot.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.f%%', shadow=True, startangle=270)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

pyplot.show()

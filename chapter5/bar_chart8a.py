import matplotlib.pyplot as pyplot
import numpy as np

labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
y_pos = np.arange(len(labels))
sizes = [45, 10, 15, 30, 22]

pyplot.bar(y_pos, sizes, align='center')
pyplot.xticks(y_pos, labels)
pyplot.ylabel('Usage')
pyplot.xlabel('Programming Languages')

pyplot.show()
import matplotlib.pyplot as plt
import numpy as np

labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
y_pos = np.arange(len(labels))
sizes = [45, 10, 15, 30, 22]

plt.bar(y_pos, sizes, align='center')
plt.xticks(y_pos, labels)
plt.ylabel('Usage')
plt.xlabel('Programming Languages')

plt.show()
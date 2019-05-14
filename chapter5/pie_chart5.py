import matplotlib.pyplot as pyplot

labels = 'Python', 'Scala', 'C#', 'Java'
sizes = [45, 10, 15, 30]

pyplot.pie(sizes, labels=labels, autopct='%1.f%%', startangle=270)

pyplot.show()

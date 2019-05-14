import matplotlib.pyplot as pyplot

labels = 'Python', 'Scala', 'C#', 'Java'
sizes = [45, 10, 15, 30]

# only "explode" the 3rd slice (i.e. 'Python')
explode = (0.1, 0, 0, 0)

pyplot.pie(sizes, explode=explode, labels=labels, autopct='%1.f%%', shadow=True, startangle=270)

pyplot.show()

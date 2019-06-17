import matplotlib.pyplot as pyplot

labels = ('Python', 'Java', 'Scala', 'C#')
sizes = [45, 30, 15, 10]

# only "explode" the 1st slice (i.e. 'Python')
explode = (0.1, 0, 0, 0)

pyplot.pie(sizes,
           explode=explode,
           labels=labels,
           autopct='%1.f%%',
           shadow=True,
           counterclock=False,
           startangle=90)

pyplot.show()

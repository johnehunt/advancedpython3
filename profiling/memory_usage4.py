from pympler import asizeof, tracker

from itertools import chain

class Student:

    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

class Subject:

    def __init__(self, title):
        self.title = title

tr = tracker.SummaryTracker()

ENGLISH = Subject('English')
ANIMATION = Subject('Animation')
COMPUTING = Subject('Computing')

class1 = [Student('Jasmine', 20, ENGLISH),
          Student('Adam', 20, ENGLISH),
          Student('Eloise', 20, ENGLISH)]

class2 = [Student('Phoebe', 22, ANIMATION),
          Student('Gryff', 22, ANIMATION)]

class3 = [Student('Tom', 24, COMPUTING),
          Student('James', 21, COMPUTING),
          Student('Andrew', 23, COMPUTING)]

year = list(chain(class1, class2, class3))

print('asizeof.asizeof([year])', asizeof.asizeof([year]))
print(asizeof.asized([year], detail=3).format())

tr.print_diff()


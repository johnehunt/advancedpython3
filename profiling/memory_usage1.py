import sys

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


print('int', sys.getsizeof(1), 'bytes')
print('float:', sys.getsizeof(1.0))

print('tuple:', sys.getsizeof((1, 2, 3)))
print('list:', sys.getsizeof([1, 2, 3]))
print('set:', sys.getsizeof({1, 2, 3}))

print('string:', sys.getsizeof('Hello World'))
print('Person:', sys.getsizeof(Person('Phoebe', 22)))



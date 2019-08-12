from memprof import *

class Person:

    def __init__(self, name, hours, hourly_rate):
        self.name = name
        self.hours = hours
        self.hourly_rate = hourly_rate

    def __str__(self):
        return 'Person' + (self.name) + ' worked ' + self.hours + ' @ ' + self.hourly_rate


def calculate_pay(person):
    x = person.hours * person.hourly_rate
    return x

@memprof
def get_pay():
    employees = [Person('Phoebe', i, 6.50) for i in list(range(0, 1000))]
    numbers = [n * n * n for n in list(range(0, 100000))]
    total = sum([calculate_pay(p) for p in employees])

    return numbers, total


if __name__ == '__main__':
    print(get_pay())

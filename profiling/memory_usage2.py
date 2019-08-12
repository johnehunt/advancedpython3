from memory_profiler import profile

precision = 5

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

@profile(precision=precision)
def get_pay():
    employees = [Person('Phoebe', 40, 6.50), Person('Gryff', 22, 5.95),
            Person('Adam', 12, 4.99), Person('Jasmine', 35, 5.95)
            ]
    numbers = [n for n in range(0, 10 ** 5) if n % 2 == 0]
    results = []
    for p in employees:
        results.append((p, calculate_pay(p)))

    total = sum([calculate_pay(p) for p in employees])

    return results, total


if __name__ == '__main__':
    print(get_pay())


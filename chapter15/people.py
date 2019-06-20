class Person:

    def calculate_pay(self):
        return 0.0

class Payroll:

    def generate_payslip(self, person):
        return 'You earned ' + str(person.calculate_pay())
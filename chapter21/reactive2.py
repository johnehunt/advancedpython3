# A subscribers example

from rx import Observable, Observer
from rx.subjects import Subject
import datetime
import time

source = Observable.from_list([2, 3, 5, 7])


class PrimeNumbersSubject(Subject):

    def on_next(self, value):
        print('Subject Received', value)
        super().on_next((value, datetime.datetime.now()))

    def on_completed(self):
        print('Data Stream Completed')
        super().on_completed()

    def on_error(self, error):
        print('In Subject - Error Occurred', error)
        super().on_error(error)


def prime_number_reporter(value):
    print('Function Received', value)


print('Set up')

# Create the Subject
subject = PrimeNumbersSubject()

# Set up subscribers for the subject
subject.subscribe(prime_number_reporter)
subject.subscribe(lambda value: print('Lambda Received', value))
subject.subscribe(
    on_next = lambda value: print('Received on_next', value),
    on_error = lambda exp: print('Error Occurred', exp),
    on_completed = lambda: print('Received completed notification')
)

# Subscribe the Subject to the observable source
source.subscribe(subject)

print('Done')

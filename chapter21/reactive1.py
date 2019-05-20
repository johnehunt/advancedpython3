from rx import Observable, Observer

source = Observable.from_list([2, 3, 5, 7])


class PrimeNumberReporter(Observer):

    def on_next(self, value):
        print('Object Received', value)

    def on_completed(self):
        print('Data Stream Completed')

    def on_error(self, error):
        print('Error Occurred', error)


def prime_number_reporter(value):
    print('Function Received', value)


print('Set up subscribers')

# Subscribe a lambda function
source.subscribe(lambda value: print('Lambda Received', value))
# Subscribe a named function
source.subscribe(prime_number_reporter)
# Subscribe an Observer object
source.subscribe(PrimeNumberReporter())

# Use lambdas to set up all three functions
source.subscribe(
    on_next = lambda value: print('Received on_next', value),
    on_error = lambda exp: print('Error Occurred', exp),
    on_completed = lambda: print('Received completed notification')
)

print('Done')
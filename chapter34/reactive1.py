import rx

print('Create the Observable object')
# Create an observable using data in a list
observable = rx.from_list([2, 3, 5, 7])


class PrimeNumberObserver:
    """ An Observer class """

    def on_next(self, value):
        print('Object Received', value)

    def on_completed(self):
        print('Data Stream Completed')

    def on_error(self, error):
        print('Error Occurred', error)


def prime_number_reporter(value):
    print('Function Received', value)


print('Set up Observers / Subscribers')

# Subscribe a lambda function
observable.subscribe(lambda value: print('Lambda Received', value))
# Subscribe a named function
observable.subscribe(prime_number_reporter)
# Subscribe an Observer object
observable.subscribe(PrimeNumberObserver())

# Use lambdas to set up all three functions
observable.subscribe(
    on_next=lambda value: print('Received on_next', value),
    on_error=lambda exp: print('Error Occurred', exp),
    on_completed=lambda: print('Received completed notification')
)

print('Done')

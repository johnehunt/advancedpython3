# Filter source for even numbers
from rx import Observable, Observer

# Set up a source with a filter
source = Observable.from_list([2, 3, 5, 7, 4, 9, 8])\
                   .filter(lambda value: value % 2 == 0)

# Subscribe a lambda function
source.subscribe(lambda value: print('Lambda Received', value))


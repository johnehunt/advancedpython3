# Apply a transformation to a data source to convert
# integers into strings
from rx import Observable, Observer

# Set up a source with a filter
source = Observable.from_list([2, 3, 5, 7])\
                   .map(lambda value: "'" + str(value) + "'")

# Subscribe a lambda function
source.subscribe(lambda value: print('Lambda Received',
                                     value,
                                     ' is a string ',
                                     isinstance(value, str)))

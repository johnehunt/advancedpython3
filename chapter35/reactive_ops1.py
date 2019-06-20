# Apply a transformation to a data source to convert
# integers into strings
import rx
from rx import operators as op

# Set up a source with a map function
source = rx.from_list([2, 3, 5, 7]).pipe(
    op.map(lambda value: "'" + str(value) + "'")
)

# Subscribe a lambda function
source.subscribe(lambda value: print('Lambda Received',
                                     value,
                                     ' is a string ',
                                     isinstance(value, str)))

# Example of chaining operators together
import rx
from rx import operators as op

# Set up a source with a filter and a map
source = rx.from_list([2, 3, 5, 7, 4, 9, 8])
pipe = source.pipe(
    op.filter(lambda value: value % 2 == 0),
    op.map(lambda value: "'" + str(value) + "'")
)

# Subscribe a lambda function
pipe.subscribe(lambda value: print('Received', value))

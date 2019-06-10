# An example illustrating how to merge two data sources
import rx
from rx import operators as op

# Set up a source with a filter
source1 = rx.from_list([2, 3, 5, 7])
source2 = rx.from_list([10, 11, 12])

rx.merge(source1, source2)\
    .subscribe(lambda v: print(v, end=','))
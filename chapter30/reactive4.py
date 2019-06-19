# An example illustrating how to merge two data sources
import rx

# Set up two sources
source1 = rx.from_list([2, 3, 5, 7])
source2 = rx.from_list([10, 11, 12])

# Use the merge function to create a single observable data stream
rx.merge(source1, source2)\
    .subscribe(lambda v: print(v, end=','))
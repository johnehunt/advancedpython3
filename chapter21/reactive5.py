# An example illustrating how to merge two data sources
from rx import Observable, Observer

# Set up a source with a filter
source1 = Observable.from_list([2, 3, 5, 7])
source2 = Observable.from_list([10,11,12])

Observable.merge(source1, source2)\
           .subscribe(lambda v: print(v))
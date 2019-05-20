# Example of summinf all the valus in a data stream
from rx import Observable, Observer

# Set up a source with a filter
source = Observable.from_list([2, 3, 5, 7]) \
        .sum() \
        .subscribe(lambda v: print(v))

print('-' * 20)

# Rolling or incremental sum
Observable.from_([1,2,3,4,5])\
          .scan(lambda subtotal, i: subtotal+i)\
          .subscribe(lambda v: print(v))
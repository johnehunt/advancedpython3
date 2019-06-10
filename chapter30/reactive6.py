# Example of summing all the values in a data stream
import rx
from rx import operators as op

# Set up a source and apply sum
rx.from_list([2, 3, 5, 7]).pipe(
    op.sum()
).subscribe(lambda v: print(v))

print('-' * 20)

# Rolling or incremental sum
rx.from_([2, 3, 5, 7]).pipe(
          op.scan(lambda subtotal, i: subtotal+i)
).subscribe(lambda v: print(v))
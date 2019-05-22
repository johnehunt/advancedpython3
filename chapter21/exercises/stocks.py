import rx
from rx import operators as op

def reporter(value):
    print(value)

stocks = (('APPL', 12.45), ('IBM', 15.55), ('MSFT', 5.66), ('APPL', 13.33))

# Select only APPL
source = rx.from_list(stocks).pipe(
    op.filter(lambda stock: stock[0] == 'APPL')
).subscribe(reporter)

print('-' * 25)

# ALl stocks over 15.00
source = rx.from_list(stocks).pipe(
    op.filter(lambda stock: stock[1] > 15.00)
).subscribe(reporter)

print('-' * 25)

# Find the average
source = rx.from_list(stocks).pipe(
    op.map(lambda v: v[1]),
    op.average()
).subscribe(reporter)

print('=' * 25)


stocks2 = (('GOOG', 8.95), ('APPL', 7.65), ('APPL', 12.45), ('MSFT', 5.66), ('GOOG', 7.56), ('IBM', 12.76))

source1 = rx.from_list(stocks)
source2 = rx.from_list(stocks2)

# Find the max
rx.merge(source1, source2).pipe(
    op.map(lambda v: v[1]),
    op.max()
).subscribe(reporter)

print('-' * 25)

# Find the min
rx.merge(source1, source2).pipe(
    op.map(lambda v: v[1]),
    op.min()
).subscribe(reporter)

print('-' * 25)

# Only publish unique values
rx.merge(source1, source2).pipe(
    op.distinct()
).subscribe(reporter)
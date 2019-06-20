# Example of a 'cold' Observable
import rx
from rx.concurrency import NewThreadScheduler
import time


def observer_function(value):
    time.sleep(1)
    print(value * value)


rx.range(1, 100000, scheduler=NewThreadScheduler())\
    .subscribe(observer_function)

# As the observable runs in a separate thread need
# ensure that the main thread does not terminate
input('Press enter to finish')
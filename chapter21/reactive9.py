# Example of a 'cold' Observable
import rx
from rx.concurrency import CurrentThreadScheduler
import time


def observer_function(value):
    time.sleep(1)
    print(value * value)


rx.range(1, 100000, scheduler=CurrentThreadScheduler())\
    .subscribe(observer_function)
import rx
from rx.concurrency import NewThreadScheduler, ThreadPoolScheduler, ImmediateScheduler

observable = rx.from_list([2, 3, 5])

observable.subscribe(lambda v: print('Lambda1 Received', v), scheduler=ThreadPoolScheduler(3))
observable.subscribe(lambda v: print('Lambda2 Received', v), scheduler=ImmediateScheduler())
observable.subscribe(lambda v: print('Lambda3 Received', v), scheduler=NewThreadScheduler())

# As the observable runs in a separate thread we need
# to ensure that the main thread does not terminate
input('Press enter to finish')

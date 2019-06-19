import rx

# Set up an observable
observable = rx.from_list([2, 3, 5])

# Subscribe three observers
observable.subscribe(lambda v: print('Lambda1 Received', v))
observable.subscribe(lambda v: print('Lambda2 Received', v))
observable.subscribe(lambda v: print('Lambda3 Received', v))

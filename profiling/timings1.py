from time import time

# decorator to time functions
def timer(func):
    def func_timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(func.__name__, 'executed in', end - start)
        return result
    return func_timer

@timer
def sample_function():
    result = 0
    for i in range(100000):
        result = result + (i * i * i)
    return result

sample_function()


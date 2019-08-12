import cProfile
import pstats

def do_cprofile(func):
    """Decorator for profiling a function """

    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            stats = pstats.Stats(profile)
            stats.strip_dirs().sort_stats("time").print_stats(20)

    return profiled_func

from random import randint
from time import sleep

def fibonacci(n):
    print('.', end='')
    if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@do_cprofile
def calculate(n):
    print('In calculate')
    for _ in range(0, n):
        fibonacci(randint(10,30))
        sleep(0.5)
        print()
    print('Done calculate')


def main():
    print('In main')
    calculate(5)
    print('Done')


print('Running')
main()
print('Done profiling')



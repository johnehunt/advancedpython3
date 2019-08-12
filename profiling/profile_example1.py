import cProfile
import pstats

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


def calculate(n):
    print('In calculate')
    for _ in range(0, n):
        fibonacci(randint(10,30))
        sleep(0.5)
        print()
    print('Done calculate')


def main():
    print('In main')
    cProfile.run('calculate(5)')
    cProfile.run('calculate(5)', 'profile_results.profile')
    print('Done')


print('Running cProfile')
main()
print('Done profiling')

p = pstats.Stats('profile_results.profile')
p.strip_dirs().sort_stats('time').print_stats()


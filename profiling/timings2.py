from timeit import timeit, Timer

def sample_function():
    result = 0
    for i in range(100000):
        result = result + (i * i * i)
    return result


time_taken = timeit(sample_function, number = 1000)
print('total time:', time_taken, ', avarage time', time_taken/1000)

print('-' * 25)

timer = Timer(sample_function)
print(timer.timeit(number = 1000))
print(timer.repeat(repeat = 5, number=1000))


from rx import Observable, Observer


class PrimeNumberGenerator:

    def __init__(self, max):
        self.max = max

    def generate(self):
        result = []
        """ Provides a sequence of prime numbers up to num"""
        # Assume a number is a prime number until proved otherwise
        prime_number = True
        for i in range(2, self.max):
            for j in range(2, i):
                # If there is no remainder then its not a prime number
                if i % j == 0:
                    prime_number = False
                    break
            if prime_number:
                result.append(i)
            prime_number = True
        return Observable.from_(result)


prime_number_generator = PrimeNumberGenerator(15)
prime_number_generator.generate().subscribe(lambda v: print('Received', v))

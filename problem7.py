import math
import time

primes = [2,3,5,7,11]
test_number = 13
def is_prime(n):
    for i in primes:
        if n%i == 0:
            return False
    primes.append(n)
    return True

while len(primes) < 10001:
    is_prime(test_number)
    test_number += 2

print(primes[10000])
    
import math
import time

start_time = time.time()
primes = [2,3,5,7,11,13,17]

def is_prime(n):
    for i in primes:
        if n % i == 0:
            return False
    primes.append(n)

def prime_array_maker():
    for i in range(19, 2000000, 2):
        is_prime(i)
    
prime_array_maker()
print(sum(primes))
end_time = time.time()
print(f"It took an uncomfortable {end_time - start_time:.6f} seconds")
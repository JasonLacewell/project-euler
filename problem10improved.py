import math
import time

start_time = time.time()

def primes_up_to_limit(n = int):
    start_remove =  int(math.sqrt(n))
    sieve = [True,True,False]
    for i in range(3, n + 1):
        sieve.append(False)
    for i in range(4, n+1, 2):
        sieve[i] = True
    for i in range(3, start_remove + 1, 2):
        if not sieve[i]:
            for j in range(i*i, n + 1, 2*i):
                sieve[j] = True
    sum = 0
    for i in range(2, n+1):
        if not sieve[i]:
            sum += i

    end_time = time.time()

    print(sum, f"It took {end_time - start_time:.6f} seconds")
            

primes_up_to_limit(2000000)
    

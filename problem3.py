#What is the largest prime factor of the number 600851475143?
import math
import time

start_time = time.time()

factors = []
def factorize(n):
   
    f = math.floor(math.sqrt(n))
    #p = f
   
    while f > 1:
        if n % f == 0:
            factorize(f)
            factorize(int(n/f))
            return
        else:
            f -= 1
    factors.append(n)

factorize(600851475143)
end_time = time.time()
print(max(factors), f"It took {end_time - start_time:.6f} seconds")
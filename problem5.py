import math
import time

start_time = time.time()
factors = []

def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def smallest_number(l):
    global factors
    for i in range(2, l + 1):
        if is_prime(i):
            j = 1
            while i**j <= l:
                factors.append(i)
                j += 1
smallest_number(20)
result = math.prod(factors)
print(result, factors)
#If we list all the natural numbers below 10 that are multiples 
#of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#This runs faster than the others!
import time

start_time = time.time()

a = {3*i for i in range(1, 334)}
b = {5*i for i in range(1, 200)}

end_time = time.time()

print(sum(a | b), f"{end_time - start_time:.6f} seconds")
#If we list all the natural numbers below 10 that are multiples 
#of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
import time

start_time = time.time()

sum = 0
i = 3
j = 5

while j <= 1000:
    while i < j:
        sum += i
        i += 3
    if i != j:
        sum += j
    j += 5
    
end_time = time.time()
print(sum - 1000, f"{end_time - start_time:.6f} seconds")




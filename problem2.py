import time

start_time = time.time()

fib_1 = 1
fib_2 = 1
fib_n = 2
even_sum = 0

while fib_n <= 4000000:

    even_sum += fib_n

    for i in range(1,4):
        fib_1 = fib_2
        fib_2 = fib_n
        fib_n = fib_1 + fib_2
        
end_time = time.time()

print(even_sum, f"{end_time - start_time:.6f} seconds")
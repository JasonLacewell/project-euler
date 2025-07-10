import math
import time
import sys
start_time = time.time()

largest_palindrome = [0, 0, 0]

def palindrome_checker(a, b):
    global largest_palindrome
    n = a*b
    n_str = str(n)
    if n < largest_palindrome[0]:
        print(largest_palindrome[0])
        sys.exit()
    for i in range(len(n_str)//2):
        if n_str[i] != n_str[-1-i]:
            return
    
    if n > largest_palindrome[0]:
        largest_palindrome[0] = n
        largest_palindrome[1] = a
        largest_palindrome[2] = b

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        palindrome_checker(i,j)
        
end_time = time.time()
print(f"{largest_palindrome[0]} = {largest_palindrome[1]} X {largest_palindrome[2]}",f"It took {end_time - start_time:.6f} seconds" )
#If we list all the natural numbers below 10 that are multiples 
#of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

n = 1
sum = 0

while n < 200:
    sum += 8*n 
    n += 1

while n < 334:
    sum += 3*n
    n += 1

n = 1

while n < 67:
    sum -= 15*n
    n += 1

print(sum)

#this just feels like I did this the hard way!
    


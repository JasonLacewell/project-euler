import math

a = 0
c = 0

for i in range(0, 1000):
    a = ((1000**2)-(2000*i))/(2000-(2*i))
    a_tail = a - math.floor(a)
    if a_tail < 0.001:
        c = math.sqrt(a**2 + i**2)
        print(a, i, a*i*c)
    
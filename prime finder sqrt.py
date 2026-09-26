import math
n = 1
while n < 1000000: # if you want it to run infinitely, replace "n < 1000000" with "True"
    n += 1
    prime = True
    sqrt = math.sqrt(n)
    f = 1
    while f < sqrt:
        f += 1
        if not n % f:
            prime = False
            break
    if prime:
        print(n)

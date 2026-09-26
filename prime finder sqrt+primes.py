import math
primes = [2]
n = 2
while n < 1000000: # if you want it to run infinitely, replace "n < 1000000" with "True"
    n += 1
    sqrt = math.sqrt(n)
    for div in primes:
        if div > sqrt:
            primes.append(n)
            print(n)
            break
        if not n % div:
            break

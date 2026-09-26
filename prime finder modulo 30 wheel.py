import math
n = 7
primes = [7]
sequence = [4, 2, 4, 2, 4, 6, 2, 6]
while n < 1000000: # if you want it to run infinitely, replace "n < 1000000" with "True"
    for change in sequence:
        n += change
        sqrt = math.sqrt(n)
        for div in primes:
            if div > sqrt:
                primes.append(n)
                print(n)
                break
            if not n % div:
                break

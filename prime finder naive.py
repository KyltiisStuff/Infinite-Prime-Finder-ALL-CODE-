n = 1
while n < 100000: # if you want it to run infinitely, replace "n < 100000" with "True"
    n += 1
    prime = True
    for f in range(2, n):
        if n % f == 0:
            prime = False
            break
    if prime:
        print(n)

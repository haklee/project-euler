from sympy import primerange

n = 10**10

i = 1
for p in primerange(1000000):  # any big number
    v = (pow(p - 1, i, p * p) + pow(p + 1, i, p * p)) % (p * p)
    if v > n:
        break
    i += 1

print(i)

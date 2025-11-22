from math import comb
from sympy import primerange

n = 51
primes = [*primerange(n)]
s = set()

for i in range(n):
    for j in range(i):
        v = comb(i, j)
        if all(v % p**2 for p in primes):
            s.add(v)

print(sum(s))

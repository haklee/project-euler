from math import log2
from sympy import primerange

a = 800800
b = 800800
limit = b * log2(a)
primes = [*primerange(int(limit))]

sol = 0
j = len(primes) - 1
for i in range(len(primes) - 1):
    if i >= j:
        break
    while primes[i] * log2(primes[j]) + primes[j] * log2(primes[i]) > limit:
        j -= 1
    sol += j - i

print(sol)

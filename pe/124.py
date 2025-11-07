from sympy import primerange

n = 10**5
t = 10**4

factors = [1 for _ in range(n + 1)]
for p in primerange(n):
    for i in range(p, n + 1, p):
        factors[i] *= p
a = sorted([(e, i) for i, e in enumerate(factors)])

print(a[t][1])

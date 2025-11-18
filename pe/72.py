from sympy import primerange

n = 10**6
a = [i for i in range(n + 1)]
for p in primerange(n + 1):
    for i in range(p, n + 1, p):
        a[i] = a[i] * (p - 1) // p
print(sum(a[2:]))

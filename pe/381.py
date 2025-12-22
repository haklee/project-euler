from sympy import primerange

n = 10**8
s = 0

for p in primerange(5, n):
    a, b, c = pow(p - 2, -1, p), pow(p - 3, -1, p), pow(p - 4, -1, p)
    x = (a + a * b + a * b * c) % p
    s += x

print(s)

from sympy import primerange

prime_lim = 100
n = 10**9
l = [1]

for p in primerange(prime_lim + 1):
    t = []
    q = p
    while q <= n:
        for i in l:
            v = i * q
            if v > n:
                break
            t.append(v)
        q *= p
    l = sorted(l + t)

print(len(l))

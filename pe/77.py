from sympy import primerange

n = 100  # test with values
d = {0: 1}
sol = 0
for p in primerange(n):
    tmp_d = {}
    for v in range(p, n, p):
        for k in d:
            if k + v < n:
                if k + v not in tmp_d:
                    tmp_d[k + v] = 0
                tmp_d[k + v] += d[k]
    for k in tmp_d:
        if k not in d:
            d[k] = 0
        d[k] += tmp_d[k]

print(min(k for k in d if d[k] >= 5000))

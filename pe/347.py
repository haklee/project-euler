from sympy import primerange

n = 10**7

primes = [*primerange(n // 2)]


def m(i, j, n):
    l = [0]
    q = [(1, 1)]
    searched = set()
    while q:
        v = q.pop()
        if not v in searched:
            searched.add(v)
            x = i ** v[0] * j ** v[1]
            if x <= n:
                l.append(x)
                q.extend([(v[0] + 1, v[1]), (v[0], v[1] + 1)])
    return max(l)


sol = 0
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        if i * j > n:
            break
        sol += m(primes[i], primes[j], n)

print(sol)

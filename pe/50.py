from sympy import primerange, isprime

lim = 1000000


def solve(lim):
    prime_list = list(primerange(lim))

    for i in range(len(prime_list), 0, -1):
        for j in range(len(prime_list) - i):
            v = sum(prime_list[j : j + i])
            if v > lim:
                break
            if v < lim and isprime(v):
                return v


print(solve(lim))

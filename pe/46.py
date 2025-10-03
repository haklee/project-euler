from sympy import isprime

primes = []
n = 3
while 1:
    if isprime(n):
        primes.append(n)
    else:
        for p in primes:
            x = int(((n - p) // 2) ** 0.5)
            if x * x * 2 == n - p:
                break
        else:
            print(n)
            break
    n += 2

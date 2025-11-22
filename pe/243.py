from sympy import primerange

primes = primerange(100)
ratio = 15499 / 94744

a = 1
b = 1
for p in primes:
    a *= p
    b *= p - 1
    if b / (a - 1) < ratio:
        a //= p
        b //= p - 1
        break

for i in range(1, p):
    if b * i / (a * i - 1) < ratio:
        print(a * i)
        break

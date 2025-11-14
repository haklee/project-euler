from sympy import primerange, isprime

max_v = 10000
primes = [3] + list(primerange(7, max_v))
n = 5

prime_y = set()
prime_n = set()


def prime_check(i, j):
    v = int(str(i) + str(j))
    if v in prime_y:
        return True
    if v in prime_n:
        return False

    if isprime(v):
        prime_y.add(v)
        return True
    else:
        prime_n.add(v)
        return False


sol = []


def backtrack(i):
    sol.append(primes[i])

    if len(sol) == n:
        print(sol, sum(sol))
        return

    for j in range(i + 1, len(primes)):
        if all(prime_check(p, primes[j]) and prime_check(primes[j], p) for p in sol):
            backtrack(j)
            sol.pop()


for i in range(len(primes)):
    sol = []
    backtrack(i)

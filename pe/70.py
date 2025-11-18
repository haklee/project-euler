from sympy import primerange

n = 10**7
a = [i for i in range(n + 1)]
for p in primerange(n + 1):
    for i in range(p, n + 1, p):
        a[i] = a[i] * (p - 1) // p

ratio = float("inf")
sol = None
for i in range(2, n + 1):
    if sorted(str(i)) == sorted(str(a[i])) and i / a[i] < ratio:
        ratio = i / a[i]
        sol = i

print(sol)

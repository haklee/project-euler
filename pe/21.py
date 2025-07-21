from sympy import divisors

a = [0] + [sum(divisors(i)[:-1]) for i in range(1, 10000)] + [0] * 100000

v = []
for i in range(10000):
    if i == a[a[i]] and i != a[i]:
        v.append(i)


print(sum(v))

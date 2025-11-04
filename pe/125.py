import math

n = 10**8
a = [i**2 for i in range((math.ceil(n**0.5)))]

for i in range(len(a) - 1):
    a[i + 1] += a[i]

sol = set()

for i in range(len(a)):
    for j in range(i - 1):
        x = a[i] - a[j]
        if x < n and str(x) == str(x)[::-1]:
            sol.add(x)

print(sum(sol))

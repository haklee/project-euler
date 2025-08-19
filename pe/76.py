n = 100

a = [0] * (n + 1)
v = range(1, n + 1)

a[0] = 1
for c in v:
    for i in range(c, n + 1):
        a[i] += a[i - c]

print(a[n] - 1)

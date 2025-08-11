a = [0] * 201
v = [1, 2, 5, 10, 20, 50, 100, 200]

a[0] = 1
for c in v:
    for i in range(c, 201):
        a[i] += a[i - c]

print(a[200])

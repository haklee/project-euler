n = 10000
a = [i * (3 * i - 1) // 2 for i in range(1, n + 1)]
s = set(a)
m = a[-1]
for i in range(n):
    for j in range(i):
        if a[i] + a[j] in s and a[i] - a[j] in s:
            m = min(m, a[i] - a[j])
            print(a[i], a[j])

print(m)

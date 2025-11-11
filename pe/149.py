n = 2000
x = [
    (100003 - 200003 * (k + 1) + 300007 * (k + 1) ** 3) % 10**6 - 5 * 10**5
    for k in range(55)
]
for i in range(55, n * n):
    x.append((x[i - 24] + x[i - 55]) % 10**6 - 5 * 10**5)

sol = 0

for i in range(n):
    s = 0
    for j in range(n):
        s += x[i * n + j]
        if s < 0:
            s = 0
        sol = max(s, sol)

for i in range(n):
    s = 0
    for j in range(n):
        s += x[i + j * n]
        if s < 0:
            s = 0
        sol = max(s, sol)

for i in range(n):
    s = 0
    for j in range(i + 1):
        s += x[j * n + (i - j)]
        if s < 0:
            s = 0
        sol = max(s, sol)

for i in range(n):
    s = 0
    for j in range(i + 1):
        s += x[(n - 1 - j) * n + (n - 1 - (i - j))]
        if s < 0:
            s = 0
        sol = max(s, sol)

for i in range(n):
    s = 0
    for j in range(i + 1):
        s += x[j + (n - 1 - (i - j)) * n]
        if s < 0:
            s = 0
        sol = max(s, sol)

for i in range(n):
    s = 0
    for j in range(i + 1):
        s += x[(n - 1 - j) + (i - j) * n]
        if s < 0:
            s = 0
        sol = max(s, sol)

print(sol)

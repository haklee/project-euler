n = 15

# a[i][j]: probability of taking i blue chips out of i+j chips
a = [[0] * (n + 1) for _ in range(n + 1)]
a[0][0] = 1

for i in range(1, n + 1):
    for j in range(i + 1):
        if j - 1 >= 0:
            a[j][i - j] += a[j - 1][i - j] / (1 + i)
        if i - j - 1 >= 0:
            a[j][i - j] += a[j][i - j - 1] * i / (1 + i)

print(int(1 / sum(a[j][n - j] for j in range(n + 1) if 2 * j > n)))

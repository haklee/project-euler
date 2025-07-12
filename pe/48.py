m = int(1e10)
n = 1000
print(sum(pow(i, i, m) for i in range(1, n + 1)) % m)

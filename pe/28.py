# condition
n = 1001

# solve
m = n // 2 + 1
print(4 * sum((i * 2 + 1) ** 2 - 3 * i for i in range(m)) - 3)

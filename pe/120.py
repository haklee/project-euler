n = 1000
sol = sum(
    max([2, *[i * j * 2 % (i * i) for j in range(1, 2 * i + 1, 2)]])
    for i in range(3, n + 1)
)

print(sol)

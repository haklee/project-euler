sol = 0
for i in range(1, 2**30 + 1):
    sol += i ^ (2 * i) ^ (3 * i) == 0

print(sol)

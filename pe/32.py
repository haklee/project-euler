sol = set()

for i in range(1, 10):
    for j in range(1000, 10000):
        if "".join(sorted(str(i) + str(j) + str(i * j))) == "123456789":
            sol.add(i * j)

for i in range(10, 100):
    for j in range(100, 1000):
        if "".join(sorted(str(i) + str(j) + str(i * j))) == "123456789":
            sol.add(i * j)

print(sum(sol))

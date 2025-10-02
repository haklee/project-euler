from itertools import combinations, product

a = [set(str(j) for j in i) for i in combinations(range(10), 6)]

sq_set = set(["01", "04", "09", "16", "25", "36", "49", "64", "81"])

sol = 0

for i in range(len(a)):
    for j in range(i + 1):
        x, y = a[i], a[j]
        if "6" in x or "9" in x:
            x.add("9")
            x.add("6")
        if "6" in y or "9" in y:
            y.add("9")
            y.add("6")
        prod = set(u + v for u, v in product(x, y)).union(
            set(u + v for u, v in product(y, x))
        )
        sol += sq_set.intersection(prod) == sq_set

print(sol)

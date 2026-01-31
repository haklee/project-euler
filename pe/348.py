square = [i**2 for i in range(1, 40000)]
d = {}
for i in range(1, 4000):
    for j in square:
        v = i**3 + j
        if v > 10**10:
            break
        d[v] = d.get(v, 0) + 1

sol = sorted([k for k in d if d[k] == 4 and str(k) == "".join(str(k)[::-1])])[:5]
print(sol)
print(sum(sol))

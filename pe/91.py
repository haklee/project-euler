from itertools import product

n = 50
sol = 0

for x1, x2, y1, y2 in product(range(n + 1), range(n + 1), range(n + 1), range(n + 1)):
    a = x1**2 + y1**2
    b = x2**2 + y2**2
    c = (x1 - x2) ** 2 + (y1 - y2) ** 2

    a, b, c = sorted([a, b, c])
    if a == 0:
        continue
    if a + b == c:
        sol += 1

# Duplicate triagles: all of the triangles are counted twice as OAB and OBA.
sol //= 2

print(sol)

# run like:
# $ python 11.py < 11.data

import math

# condition
n = 4

# init
a = [[0] * (n - 1) + [*map(int, i.split())] + [0] * (n - 1) for i in [*open(0)]]
a = [[0] * len(a[0])] * (n - 1) + a + [[0] * len(a[0])] * (n - 1)

# solve
sol = 0
for i in range(len(a) - (n - 1)):
    for j in range(len(a[0]) - (n - 1)):
        w = math.prod(a[i][j + v] for v in range(n))
        x = math.prod(a[i + v][j] for v in range(n))
        y = math.prod(a[i + v][j + v] for v in range(n))
        z = math.prod(a[i + n - v - 1][j + v] for v in range(n))
        sol = max(sol, w, x, y, z)

print(sol)

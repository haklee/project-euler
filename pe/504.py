from math import gcd

m = 100


def strictly_inside_tri(x, y):
    # points in x by y rectangle
    pts = (x + 1) * (y + 1)

    # points on diagonal
    pts -= gcd(x, y) + 1

    # points in triangle
    pts //= 2

    return pts


t = []
sol = 0

for a in range(1, m + 1):
    for b in range(1, m + 1):
        for c in range(1, m + 1):
            for d in range(1, m + 1):
                v = (
                    strictly_inside_tri(a, b)
                    + strictly_inside_tri(b, c)
                    + strictly_inside_tri(c, d)
                    + strictly_inside_tri(d, a)
                )

                # points on x, y axises are counted twice.
                v -= a + b + c + d

                # origin point
                v += 1

                if v == int(v**0.5) ** 2:
                    sol += 1

print(sol)

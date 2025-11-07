from math import gcd


def ix(x1, y1, x2, y2, x3, y3, x4, y4):
    try:
        d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if d == 0:
            return None

        t = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3))
        if 0 < t / d < 1 and 0 < u / d < 1:
            x, y, z = (t * (x2 - x1) + d * x1, t * (y2 - y1) + d * y1, d)
            if z < 0:
                x, y, z = -x, -y, -z
            g = gcd(x, y, z)
            return (x // g, y // g, z // g)
    except:
        None


def num_gen():
    m1 = 50515093
    m2 = 500
    s = 290797
    while 1:
        s = s * s % m1
        yield s % m2


n = 5000
sol = 0
segs = []
g = num_gen()
for i in range(n):
    x1, y1, x2, y2 = [next(g) for _ in range(4)]
    segs.append((x1, y1, x2, y2))


from itertools import product

pts = set()
for x, y in product(segs, segs):
    if pt := ix(*x, *y):
        pts.add(pt)

print(len(pts))

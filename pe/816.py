from math import dist
from itertools import combinations


def strip_min_dist(pts, d):
    pts = sorted(pts, key=lambda pt: pt[1])
    min_dist = d
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            if (pts[j][1] - pts[i][1]) < min_dist:
                min_dist = min(min_dist, dist(pts[i], pts[j]))
            else:
                break
    return min_dist


def min_dist(pts, s, e):
    if e - s <= 4:
        pairs = [*combinations(pts[s:e], 2)]
        if pairs:
            return min(dist(i, j) for i, j in combinations(pts[s:e], 2))
        else:
            return float("inf")
    m = (s + e) // 2
    m_x = pts[m][0]

    d = min(min_dist(pts, s, m), min_dist(pts, m, e))

    strip = [pts[i] for i in range(s, e) if abs(pts[i][0] - m_x) < d]
    return min([d, strip_min_dist(strip, d)])


n = 2000000
s = 290797
pts = []
for _ in range(n):
    t = s * s % 50515093
    pts.append((s, t))
    s = t * t % 50515093

print(min_dist(sorted(pts), 0, len(pts)))

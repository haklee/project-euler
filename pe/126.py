from heapq import heappop, heappush

n = 1000
q = []
d = {}
processed = set()

# cuboid: (cell_cnt, width, depth, height, layer_num)
heappush(q, (6, 1, 1, 1, 1))
processed.add((1, 1, 1))

limit = 20000  # test with other numbers
while q:
    cnt, i, j, k, l = heappop(q)
    if not cnt in d:
        d[cnt] = 0
    d[cnt] += 1

    # next layer
    cnt += 4 * (i + j + k) + 8 * (l - 1)
    if cnt <= limit:
        heappush(q, (cnt, i, j, k, l + 1))

    # new cuboids
    for candidate in [(i + 1, j, k), (i, j + 1, k), (i, j, k + 1)]:
        s, t, u = candidate
        if (
            candidate not in processed
            and s >= t >= u
            and 2 * (s * t + t * u + u * s) <= limit
        ):
            processed.add(candidate)
            heappush(q, (2 * (s * t + t * u + u * s), s, t, u, 1))

print(sorted([k for k in d if d[k] == n]))

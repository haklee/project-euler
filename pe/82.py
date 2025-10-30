# run like:
# $ python 82.py < 82.data

m = [(-1, 0), (1, 0), (0, 1)]


def f(x):
    q = [x]
    while q:
        i, j = q.pop(0)
        for d in m:
            u, v = i + d[0], j + d[1]
            if not (-1 < u < n and -1 < v < n):
                continue
            k = b[i][j] + a[u][v]
            if b[u][v] > k:
                b[u][v] = k
                q.append((u, v))
    return min(b[i][n - 1] for i in range(n))


a = [[*map(int, s.split(","))] for s in open(0)]
n = len(a)
c = []

for i in range(n):
    b = [[1e9] * n for _ in range(n)]
    b[i][0] = a[i][0]
    c.append(f((i, 0)))
print(min(c))

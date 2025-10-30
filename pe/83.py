# run like:
# $ python 83.py < 83.data

m = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def f():
    q = [(0, 0)]
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
    return b[n - 1][n - 1]


a = [[*map(int, s.split(","))] for s in open(0)]
n = len(a)
b = [[1e9] * n for _ in range(n)]
b[0][0] = a[0][0]
print(f())

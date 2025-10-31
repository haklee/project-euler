# run like:
# $ python 96.py < 96.data

b = [*open(0)]
sol = 0

for l in range(len(b) // 10):
    a = [[*map(int, s[:9])] for s in b[l * 10 + 1 : l * 10 + 10]]
    r, c, s = (
        [set() for _ in range(9)],
        [set() for _ in range(9)],
        [set() for _ in range(9)],
    )
    z = []

    def update(i, j, t):
        a[i][j] = t
        r[i].add(t)
        c[j].add(t)
        s[i // 3 * 3 + j // 3].add(t)

    def check(i, j, t):
        return t in r[i] or t in c[j] or t in s[i // 3 * 3 + j // 3]

    def undo(i, j, t):
        a[i][j] = 0
        r[i].remove(t)
        c[j].remove(t)
        s[i // 3 * 3 + j // 3].remove(t)

    for i in range(9):
        for j in range(9):
            v = a[i][j]
            if v:
                update(i, j, v)
            else:
                z += [(i, j)]
    z += [None]

    def f(k):
        if not z[k]:
            return int("".join(map(str, a[0][:3])))
        u, v = z[k]
        for n in range(1, 10):
            if not check(u, v, n):
                update(u, v, n)
                res = f(k + 1)
                if res:
                    return res
                else:
                    undo(u, v, n)

    sol += f(0)

print(sol)

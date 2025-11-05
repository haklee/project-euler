def f(n):
    if int(n**0.5) ** 2 == n:
        return 0

    x = int(n**0.5)
    v = (x, x, 1)

    q = []
    while 1:
        k = (n - v[1] ** 2) // v[2]
        i = int(v[2] / (n**0.5 - v[1]))
        j = -(v[1] - i * k)
        v = (i, j, k)
        if q and q[0] == v:
            break
        q.append(v)

    return len(q)


n = 10**4

print(sum(f(i) % 2 == 1 for i in range(1, n + 1)))

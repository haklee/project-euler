def t(n):
    return n * (n + 1) // 2


def p(n):
    return n * (3 * n - 1) // 2


def h(n):
    return n * (2 * n - 1)


i = j = k = 1
cnt = 3
sol = None

while cnt:
    a = (t(i), p(j), h(k))
    if len(set(a)) == 1:
        sol = a[0]
        cnt -= 1
        i += 1
        j += 1
        k += 1
        continue

    m = min(a)
    if m == a[0]:
        i += 1
    elif m == a[1]:
        j += 1
    elif m == a[2]:
        k += 1

print(sol)

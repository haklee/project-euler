def f(i):
    return "".join(sorted(str(i)))


def solve():
    d = 1
    while 1:
        for i in range(10**d, 10 ** (d + 1) // 6 + 1):
            if len(set([f(i * j) for j in range(1, 7)])) == 1:
                return i
        d += 1


print(solve())

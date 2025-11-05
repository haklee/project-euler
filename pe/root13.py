def f(n, l):
    if int(n**0.5) ** 2 == n:
        return 0
    s = str(int(n**0.5))
    i = 1
    while len(s) < l:
        for j in range(1, 10):
            x = int(s + str(j))
            if x**2 > n * 10 ** (2 * i):
                j -= 1
                break
        s += str(j)
        i += 1
    return sum(int(c) for c in s)


print(f(13, 1000 + 1) - int(13**0.5))

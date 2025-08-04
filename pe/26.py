def f(v):
    i = v
    while i % 2 == 0:
        i //= 2
    while i % 5 == 0:
        i //= 5
    x = 1
    while 1:
        if (10**x - 1) % i == 0:
            return (x, v)
        x += 1


print(max([f(i) for i in range(2, 1000)])[1])

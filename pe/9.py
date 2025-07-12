def f():
    for i in range(1000):
        for j in range(i):
            for k in range(j):
                if i + j + k == 1000 and j * j + k * k == i * i:
                    return i * j * k
    return -1


print(f())

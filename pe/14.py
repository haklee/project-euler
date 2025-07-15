# init
d = {1: 1}

# condition
v = 10**6


# solve
def f(i):
    if i == 1:
        pass
    elif i % 2 == 0:
        d[i] = f(i // 2) + 1
    else:
        d[i] = f(3 * i + 1) + 1
    return d[i]


for i in range(1, v):
    f(i)

print(max(d, key=d.get))

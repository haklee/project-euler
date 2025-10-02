factorial = [1]

for i in range(1, 10):
    factorial.append(factorial[-1] * i)

d = {169: 3, 363601: 3, 1454: 3, 871: 2, 45361: 2, 872: 2, 45362: 2}


def f(i):
    if i not in d:
        v = sum(factorial[int(j)] for j in str(i))
        if i == v:
            d[i] = 1
        else:
            d[i] = 1 + f(v)
    return d[i]


print(sum(f(i) == 60 for i in range(1, 1000000)))

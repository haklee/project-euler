from decimal import Decimal


def f(x):
    return int(x) * (x - int(x) + 1)


def diff(theta):
    a = []
    b = theta
    for _ in range(200):
        a.append(int(b))
        b = f(b)

    x = Decimal(f'{a[0]}.{"".join([str(i)for i in a[1:]])}')
    return x - theta


start, end = Decimal(2), Decimal(3)
for i in range(1000):
    mid = (start + end) / 2
    if diff(mid) > 0:
        start = mid
    else:
        end = mid
print(mid)

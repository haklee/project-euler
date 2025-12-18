from math import e, log, ceil, floor, gcd

n = 10000
r = 0

for i in range(5, n + 1):
    v = i / e
    v_ceil = ceil(v)
    v_floor = floor(v)

    x = [v_floor, v_ceil][v_ceil * log(i / v_ceil) > v_floor * log(i / v_floor)]
    x //= gcd(i, x)
    while x % 2 == 0:
        x //= 2
    while x % 5 == 0:
        x //= 5

    r += i * (1 if x != 1 else -1)

print(r)

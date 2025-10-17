from math import ceil

n = 10**6

sol = 0
for a in range(3, int(n / 4) + 2):
    l, h = 1, (a - 1) // 2
    while l < h:
        m = ceil((l + h) / 2)
        b = a - 2 * m
        if a * a - b * b == n:
            h = m
            break
        elif a * a - b * b < n:
            l = m
        else:
            h = m - 1
    sol += h

print(sol)

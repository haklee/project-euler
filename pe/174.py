n = 10**6

type_l = [0 for _ in range(n + 1)]

for t in range(1, n):
    for i in range(1, n):
        tile_num = (i + 2 * t) ** 2 - i**2
        if tile_num <= n:
            type_l[tile_num] += 1
        else:
            break
    if i == 1:
        break

print(len([i for i in type_l if 0 < i < 11]))

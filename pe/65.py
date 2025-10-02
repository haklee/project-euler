a, b, c, d = 2, 1, 3, 1

t, i = 100, 0

while i < t - 2:
    i += 1
    k = 2 * (i // 3 + 1) if i % 3 == 1 else 1
    a, b, c, d = c, d, a + k * c, b + k * d

print(sum([int(i) for i in str(c)]))

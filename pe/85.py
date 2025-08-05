l = []

i = 2
while 1:
    x = i * (i - 1) // 2
    if x > 2 * 10**6:
        break
    l.append(x)
    i += 1

print(
    min(
        (abs((2 * 10**6 - l[i] * l[j])), ((i + 1) * (j + 1)))
        for i in range(len(l))
        for j in range(len(l))
    )[1]
)

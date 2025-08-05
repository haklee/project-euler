v = 0

for i in range(3, 10):
    l = [*range(1, i)]
    x = 1
    while 1:
        s = ""
        for j in l:
            s += str(x * j)
        if len(s) >= 10:
            break
        if all(str(j) in s for j in range(1, 10)):
            v = max(v, int(s))
        x += 1

print(v)

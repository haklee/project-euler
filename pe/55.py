s = 0
t = 50

for i in range(10**4):
    for _ in range(t):
        i = i + int("".join(reversed(str(i))))
        if str(i) == "".join(reversed(str(i))):
            break
    else:
        s += 1

print(s)

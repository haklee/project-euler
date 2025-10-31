def check_int(a, b, c):
    v = (a + b) ** 2 + c**2
    return v == int(v**0.5) ** 2


c = 0
cnt = 0

while cnt <= 10**6:
    c += 1
    for a in range(1, c + 1):
        for b in range(a, c + 1):
            cnt += check_int(a, b, c)

print(c)

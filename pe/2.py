s = 0
a, b = 1, 1
while b < 4e6:
    s += (b % 2 == 0) * b
    a, b = b, a + b
print(s)

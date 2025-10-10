from math import gcd

l = 12000

s = 0
for i in range(2, l + 1):
    for j in range(int(i / 3), int(i / 2) + 1):
        if gcd(i, j) == 1 and 3 * j > i and 2 * j < i:
            s += 1
print(s)

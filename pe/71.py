from math import gcd

x = 1000000
a = []

for i in range(2, x + 1):
    j = i * 3 // 7
    while gcd(i, j) != 1 and j > 0:
        j -= 1
    a.append((j, i))

a.sort(key=lambda x: x[0] / x[1])
print(a[-2][0])

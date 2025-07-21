from math import gcd

p = q = 1
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if k * (10 * j - i) == 9 * i * j and not (i == j == k):

                p *= min(10 * k + i, 10 * j + k)
                q *= max(10 * k + i, 10 * j + k)
print(p, q)
print(q / gcd(p, q))

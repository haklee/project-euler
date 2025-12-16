from math import comb

n = 100

print((comb(n + 10 - 1, n) - 1) + (comb(n + 11 - 1, n) - (n + 1)) - (n * 9))

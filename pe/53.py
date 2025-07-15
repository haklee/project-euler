from math import comb

print(sum(1 for i in range(1, 101) for j in range(i + 1) if comb(i, j) > 10**6))

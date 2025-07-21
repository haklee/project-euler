from math import prod

s = "".join([str(i) for i in range(1, 10**6)])
print(prod([int(s[i]) for i in [10**j - 1 for j in range(7)]]))

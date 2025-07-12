# run like:
# $ python 8.py < 8.data

from math import prod

s = input()
n = 13
print(max(prod(map(int, i)) for i in zip(*[s[j:] for j in range(n)])))

# run like:
# $ python 99.py < 99.data

from math import log

a = [[*map(int, s.split(","))] for s in open(0)]
a = [(e[1] * log(e[0]), i) for i, e in enumerate(a, 1)]

print(max(sorted(a))[1])

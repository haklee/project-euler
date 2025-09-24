# run like:
# $ python 81.py < 81.data

from math import inf

a = [[inf] * 81] + [[inf, *map(int, i.split(","))] for i in open(0)]

for i in range(80):
    for j in range(80):
        if i == 0 and j == 0:
            continue
        a[i + 1][j + 1] += min(a[i][j + 1], a[i + 1][j])

print(a[80][80])

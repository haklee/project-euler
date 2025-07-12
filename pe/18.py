# run like:
# $ python 18.py < 18.data

a = [[0, 0]] + [[0, *map(int, i.split()), 0] for i in open(0)]
for i in range(1, len(a)):
    for j in range(1, len(a[i]) - 1):
        a[i][j] += max(a[i - 1][j - 1 : j + 1])

print(max(a[-1]))

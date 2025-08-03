from math import factorial

v = 10**6

v -= 1
a = []
for i in range(9, -1, -1):
    j = 0
    while 1:
        if v >= factorial(i):
            j += 1
            v -= factorial(i)
        else:
            break
    a.append(j)

s = ""
n = list(range(10))
for i in a:
    j = n.pop(i)
    s += str(j)

print(s)

n = 50

a = [1, 1, 2, 4]

for i in range(3, n):
    a = [*a[1:], a[-1] + a[-2] + a[-3] + a[-4]]

print(a[-1])

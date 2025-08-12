from math import prod

n = 10**7
a = [{} for _ in range(n + 1)]
for i in range(2, n + 1):
    if not a[i].keys():
        v = i
        while v < n:
            for j in range(v, n + 1, v):
                if i in a[j]:
                    a[j][i] += 1
                else:
                    a[j][i] = 1
            v *= i

a = [prod(j + 1 for j in i.values()) for i in a]

print(sum(a[i] == a[i + 1] for i in range(2, n)))

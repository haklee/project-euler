# condition
n = 10**7

# init
a = [0] * (n + 1)
a[1], a[89] = 1, 89


# solve
def f(i):
    if not a[i]:
        a[i] = f(sum(int(j) ** 2 for j in str(i)))
    return a[i]


for i in range(1, n + 1):
    f(i)

print(sum(i == 89 for i in a))

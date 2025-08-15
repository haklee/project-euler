# run like:
# $ python 42.py < 42.data

a = [sum(ord(j) - ord("A") + 1 for j in i[1:-1]) for i in input().split(",")]

b = [0] * (max(a) + 1)

i = 0
while (v := i * (i + 1) // 2) <= max(a):
    b[v] = 1
    i += 1

print(sum(b[i] for i in a))

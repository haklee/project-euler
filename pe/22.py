# run like:
# $ python 22.py < 22.data

a = sorted(input().split(","))
x = 0
for i, s in enumerate(a, 1):
    x += sum(ord(c) - ord("A") + 1 for c in s[1:-1]) * i

print(x)

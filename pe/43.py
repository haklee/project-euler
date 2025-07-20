from itertools import product, permutations

a17 = [
    str(i).zfill(3)
    for i in range(1000)
    if i % 17 == 0 and len(set(str(i).zfill(3))) == 3
]
a13 = [
    str(i).zfill(3)
    for i in range(1000)
    if i % 13 == 0 and len(set(str(i).zfill(3))) == 3
]
a11 = [
    str(i).zfill(3)
    for i in range(1000)
    if i % 11 == 0 and len(set(str(i).zfill(3))) == 3
]
a7 = [
    str(i).zfill(3)
    for i in range(1000)
    if i % 17 == 0 and len(set(str(i).zfill(3))) == 3
]

x = [
    v
    for i, j, k, s in product(a7, a11, a13, a17)
    if i[1:] == j[:2]
    and j[1:] == k[:2]
    and k[1:] == s[:2]
    and len(set(v := i + s)) == 6
]
print(
    x
)  # ['340782', '357289', '374816', '493510', '680391', '731952', '867153', '935204', '952867']

# d_6 % 5 == 0
x = [i for i in x if int(i[1]) % 5 == 0]
print(x)  # ['357289', '952867']

sol = 0

# Case #1
# last 6 digit: 357289
# then, first 4 digits are: ['0', '1', '4', '6']

for s in ["".join(i) + "357289" for i in permutations("0146")]:
    if sum(int(i) for i in s[2:5]) % 3 == 0 and int(s[3]) % 2 == 0:
        print(s)
        sol += int(s)

# Case #2
# last 6 digit: 952867
# then, first 4 digits are: ['0', '1', '3', '4']

for s in ["".join(i) + "952867" for i in permutations("0134")]:
    if sum(int(i) for i in s[2:5]) % 3 == 0 and int(s[3]) % 2 == 0:
        print(s)
        sol += int(s)

print("---")
print(sol)

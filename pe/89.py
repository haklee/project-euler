sol = 0

for _ in range(1000):
    s = input()

    # get value
    v = 0
    if "CM" in s:
        s = s.replace("CM", "OO")
        v += 900
    if "CD" in s:
        s = s.replace("CD", "OO")
        v += 400
    if "XC" in s:
        s = s.replace("XC", "OO")
        v += 90
    if "XL" in s:
        s = s.replace("XL", "OO")
        v += 40
    if "IX" in s:
        s = s.replace("IX", "OO")
        v += 9
    if "IV" in s:
        s = s.replace("IV", "OO")
        v += 4

    v += s.count("M") * 1000
    v += s.count("D") * 500
    v += s.count("C") * 100
    v += s.count("L") * 50
    v += s.count("X") * 10
    v += s.count("V") * 5
    v += s.count("I") * 1

    # get length of minimal form
    min_l = (
        sum(
            [0, 1, 2, 3, 2, 1, 2, 3, 4, 2][int(c)] for c in str(v)[::-1][:3]
        )  ## reversed string to eliminate 4th digit
        + v // 1000
    )
    sol += len(s) - min_l

print(sol)

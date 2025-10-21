import sys

sys.set_int_max_str_digits(100000)
a = b = 1
c = 2
while 1:
    c += 1
    a, b = b, a + b
    if "".join(sorted(str(b % 10**9))) == "123456789":
        # print(c)
        if "".join(sorted(str(b // 10**9)[:9])) == "123456789":
            break

print(c)

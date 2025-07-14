from sympy import divisor_count

i = 1

while 1:
    v = (i * (i + 1)) // 2
    if divisor_count(v) > 500:
        print(v)
        break
    i += 1

def checker(i):
    s = str(i)
    b = bin(i) + "b0"
    return s == "".join(reversed(s)) and b == "".join(reversed(b))


print(sum(i for i in range(1, 10**6, 2) if checker(i)))

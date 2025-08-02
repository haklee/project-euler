v = 10**8

while 1:
    # last digit is 3
    x = v + 3
    s = str(x**2)
    if all(s[i * 2] == str(i + 1) for i in range(8)):
        print(x**2 * 100)
        break

    # last digit is 7
    x = v + 7
    s = str(x**2)
    if all(s[i * 2] == str(i + 1) for i in range(8)):
        print(x * 10)
        break

    v += 10

n = x = 0
while 1:
    n += 1
    r = sorted(str(n))
    x += n != int("".join(r)) and n != int("".join(reversed(r)))
    if x * 100 == n * 99:
        break
print(n)

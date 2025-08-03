from math import log10

v = 678910
d = 123
y = 0
while 1:
    y += 1
    start = int((y + log10(d)) / log10(2))
    end = int((y + log10(d + 1)) / log10(2))

    l = end - start
    if l <= 0:
        continue
    if v > l:
        v -= l
    else:
        print(start + v)
        break

# this runs for about a minute.

from sympy import primefactors

i = 2

while 1:
    if all(len(primefactors(i)) == 4 for i in range(i, i + 4)):
        print(i)
        break
    i += 1

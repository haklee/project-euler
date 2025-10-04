from sympy import primerange

sol = []
s = set()
x = 0
while 1:
    a = [p**2 for p in primerange(int(10**x), int(10 ** (x + 1)))]

    for i in a:
        s.add(i)

    is_done = False
    for v in a:
        u = int("".join(reversed(str(v))))
        if v != u and u in s:
            sol.append(v)
            if len(sol) == 50:
                is_done = True
                break

    if is_done:
        break

    # print(len(sol), sol)
    x += 1

print(sum(sol[:50]))

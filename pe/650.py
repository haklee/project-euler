from sympy import factorint

num = 20000
mod = int(1e9 + 7)
factored = {i: factorint(i) for i in range(1, num + 1)}
sol = 0

for n in range(1, num + 1):
    # numbers which are multiplied in B(n)

    b = {i: -n + 2 * i - 1 for i in range(2, n + 1)}

    # factorize B(n)

    p = {}
    for x in b:
        for k in factored[x]:
            p[k] = p.get(k, 0) + factored[x][k] * b[x]

    p = {k: p[k] for k in p if p[k]}

    # sum of divisors

    cur_sol = 1
    for k in p:
        v = (pow(k, p[k] + 1, mod) - 1) * pow(k - 1, -1, mod)
        cur_sol *= v
        cur_sol %= mod

    sol += cur_sol
    sol %= mod

print(sol)

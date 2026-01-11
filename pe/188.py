from sympy import totient


def f(base, hyper, mod):
    if totient(mod) == 1:
        return 1
    return pow(base, f(base, hyper - 1, int(totient(mod))) % int(totient(mod)), mod)


print(f(1777, 1855, 100000000))

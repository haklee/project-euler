t = 1000
a, b = 2, 3
sol = 0
while t != 1:
    t -= 1
    a, b = a + b, 2 * a + b
    sol += len(str(a)) < len(str(b))
print(sol)

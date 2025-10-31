n = 10**14
m = 1234567891
sol = 0

sol += pow(2, n - 1, m) * (n * (n + 1) // 2) % m

v = 0

for k in range(1, int(n**0.5) + 1):
    x = n // k
    y = n // (k + 1)
    z = (x * (x + 1) // 2 - y * (y + 1) // 2) % m
    t = pow(2, n - k, m) * z
    # print(f'2^{n-k}, {x}-{y+1}')
    v = (v + t) % m

print("here")

for k in range(1, int(n**0.5)):
    i = n // k
    t = pow(2, n - i, m)
    # print(f'2^{n-i}: {k}')
    v = (v + k * t) % m

sol = (sol - v) % m

print(sol)

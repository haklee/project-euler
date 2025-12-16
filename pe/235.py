s, e = 1, 1.1
t = -6 * 10**11
while 1:
    m = (s + e) / 2
    v = sum((900 - 3 * k) * m ** (k - 1) for k in range(1, 5000 + 1))
    print(m, v)
    if abs(t - v) < 1:
        break
    if t > v:
        e = m
    else:
        s = m

print(f"{m:.12f}")

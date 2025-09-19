def is_prime(n):

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


sol = set([2, 3, 5, 7])

for i in range(2, 1000000):
    if i in sol:
        continue

    s = str(i)
    for c in s:
        if c in "245680":
            break
    else:
        candidates = [s[i:] + s[:i] for i in range(len(s))]
        if all(is_prime(int(p)) for p in candidates):
            for p in candidates:
                sol.add(int(p))

print(len(sol))

def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


sol = []

p = 10
while len(sol) < 11:
    s = str(p)
    candidates = [s[i:] for i in range(len(s))] + [s[:i] for i in range(len(s))]
    if all(is_prime(int(i)) for i in candidates if i != ""):
        sol.append(p)
    p += 1

print(sum(sol))

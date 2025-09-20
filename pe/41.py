def is_prime(n):

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


t = 8
sol = None

while not sol:
    for i in range(int(str(t) * (t - 1) + "9"), 10 ** (t - 1), -2):
        if all(str(j) in str(i) for j in range(1, t + 1)) and is_prime(i):
            sol = i
            break
    t -= 1

print(sol)

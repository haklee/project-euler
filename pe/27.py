prime_dict = {}


def is_prime(n):
    if n not in prime_dict:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime_dict[n] = False
                break
        else:
            prime_dict[n] = True

    return prime_dict[n]


max_len = 0
sol = None

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        x = 0
        while True:
            n = x * x + a * x + b
            if n > 0 and is_prime(n):
                x += 1
            else:
                break
        if x > max_len:
            max_len = x
            sol = a * b

print(sol)

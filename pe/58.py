def is_prime(n):

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


layer = 1
all_diag_cnt = 1
prime_cnt = 0

while True:
    layer += 2
    all_diag_cnt += 4
    prime_cnt += sum(is_prime(layer**2 - (layer - 1) * i) for i in range(4))
    if prime_cnt / all_diag_cnt < 1 / 10:
        break

print(layer)

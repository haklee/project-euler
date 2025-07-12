import math

n = 600851475143
p = []
while 1:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p.append(i)
            n //= i
            break
    else:
        p.append(n)
        break
print(max(p))

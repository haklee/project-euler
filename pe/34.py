from math import factorial

f = [factorial(i) for i in range(10)]
print(sum(i for i in range(10, 10**7) if i == sum(f[(int(j))] for j in str(i))))

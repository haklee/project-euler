from sympy import divisor_sigma

a = [i for i in range(2, 28123) if divisor_sigma(i) - i > i]

sums = set(i + j for i in a for j in a)
print(sum(set(range(28123)) - sums))

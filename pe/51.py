from sympy import primerange

primes = set(primerange(10**5, 10**6))

patterns = [
    "ab***c",
    "a*b**c",
    "*ab**c",
    "a**b*c",
    "*a*b*c",
    "**ab*c",
    "a***bc",
    "*a**bc",
    "**a*bc",
    "***abc",
]


def f(pattern):
    for a in range(10):
        for b in range(10):
            for c in [1, 3, 7, 9]:
                q = (
                    pattern.replace("a", str(a))
                    .replace("b", str(b))
                    .replace("c", str(c))
                )
                numbers = [int(q.replace("*", str(i))) for i in range(10)]
                numbers = [i for i in numbers if i in primes]
                if len(numbers) == 8:
                    return numbers


sol = float("inf")

for p in patterns:
    numbers = f(p)
    if numbers:
        sol = min(sol, min(numbers))

print(sol)

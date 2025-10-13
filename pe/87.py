from sympy import primerange
from bisect import bisect_left

n = 5 * 10**7
p_square_candidates = [*primerange(int(n**0.5) + 1)]

p_a = [*primerange(int(n ** (1 / 4)) + 1)]  # last item: 83
p_b = [*primerange(int(n ** (1 / 3)) + 1)]  # last item: 367

sol = set()
for i in p_a:
    for j in p_b:
        v = i**4 + j**3
        if v > n:
            break
        ind = bisect_left(p_square_candidates, (n - v) ** 0.5)
        for k in p_square_candidates[:ind]:
            sol.add(v + k**2)

print(len(sol))

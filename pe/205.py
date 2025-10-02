from itertools import product
from collections import Counter

a = product(*[range(1, 5)] * 9)
b = product(*[range(1, 7)] * 6)
len_a = 4**9
len_b = 6**6
counter_a = Counter(sum(i) for i in a)
counter_b = Counter(sum(i) for i in b)

sol = 0

for i in counter_a:
    for j in counter_b:
        if i > j:
            sol += counter_a[i] * counter_b[j]

print(round((sol / (len_a * len_b)) * 10**7) / 10**7)

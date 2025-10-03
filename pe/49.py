from itertools import combinations
from collections import Counter
from sympy import primerange

# find 4 digit primes
primes = primerange(1000, 10000)

# find permutation sets
a = [("".join(sorted(str(p))), p) for p in primes]
d = {}
for i in a:
    k, p = i
    if k not in d:
        d[k] = []
    d[k].append(p)

# filter permutation sets so at least 3 primes are permutations of each other
d = {k: d[k] for k in d if len(d[k]) >= 3}

# diff of two primes must appear at least twice for every diff combination in the permutation set
candidates = []
for k in d:
    counter = Counter(abs(i - j) for i, j in combinations(d[k], 2))
    if any(i == 2 for i in counter.values()):
        candidates.append([d[k], [kk for kk in counter if counter[kk] == 2]])

# check if p-d, p, p+d are in the permutation set
for i in candidates:
    p_list, diff_list = i
    for p in p_list:
        for d in diff_list:
            if p + d in p_list and p - d in p_list:
                print(p - d, p, p + d)

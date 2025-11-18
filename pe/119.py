from heapq import heappop, heappush

n = 30
sol = []
max_base = 2
q = [(2, 2, 1)]

while len(sol) < n:
    num, base, exp = heappop(q)
    if sum(map(int, str(num))) == base and num > 9:
        sol.append(num)
        print(num, base, exp)
    heappush(q, (pow(base, exp + 1), base, exp + 1))

    v = 0
    for i in range(max_base + 1, int(num**0.5) + 1):
        v = i
        heappush(q, (i * i, i, 2))

    max_base = max(v, max_base)

print(sol[-1])

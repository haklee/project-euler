l, h = 32, 10

# ways to make a line
line = []
q = [[2], [3]]
while q:
    i = q.pop()
    for t in [2, 3]:
        x = i + [i[-1] + t]
        if x[-1] > l:
            continue
        elif x[-1] == l:
            line.append(i)
        else:
            q.append(x)

# possible neighboring line.
neighbor_indices = [[] for _ in range(len(line))]
for i in range(len(line)):
    for j in range(i):
        s1, s2 = set(line[i]), set(line[j])
        if len(s1.union(s2)) == len(s1) + len(s2):
            neighbor_indices[i].append(j)
            neighbor_indices[j].append(i)

# DP
dp = [1] * len(line)
for _ in range(h - 1):
    tmp_dp = [sum(dp[ind] for ind in neighbor_indices[i]) for i in range(len(line))]
    dp = tmp_dp

print(sum(dp))

d = {
    "tri": lambda i: i * (i + 1) // 2,
    "squ": lambda i: i * i,
    "pen": lambda i: i * (3 * i - 1) // 2,
    "hex": lambda i: i * (2 * i - 1),
    "hep": lambda i: i * (5 * i - 3) // 2,
    "oct": lambda i: i * (3 * i - 2),
}

candidates = []

for k in d:
    candidates += [(k, str(i)) for i in map(d[k], range(1000)) if 999 < i < 10000]

link_dict = {
    i: [j for j in candidates if i[0] != j[0] and i[1][2:] == j[1][:2]]
    for i in candidates
}

sol = []


def backtrack(i):
    sol.append(i)
    if len(sol) == 6:
        if sol[0] in link_dict[i] and len(set([j[0] for j in sol])) == 6:
            return True
        else:
            sol.pop()
            return False

    for j in link_dict[i]:
        if j not in sol:
            if backtrack(j):
                return True
    sol.pop()


for i in candidates:
    if backtrack(i):
        break

print(sum(int(i[1]) for i in sol))

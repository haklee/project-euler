# run like:
# $ python 107.py < 107.data

# Kruskal

a = [s.split(",") for s in [*open(0)]]
n = len(a)
edges = []

for i in range(n):
    for j in range(i):
        if a[i][j] != "-":
            edges.append((i, j, int(a[i][j])))

edges.sort(key=lambda x: x[2])

parent_list = [x for x in range(n)]


def get_parent(x):
    if x == parent_list[x]:
        return x
    else:
        return get_parent(parent_list[x])


weight, found_edge_num = 0, 0

for a, b, value in edges:
    p_a, p_b = get_parent(a), get_parent(b)
    if p_a != p_b:
        # union
        parent_list[p_b] = p_a

        weight += value
        found_edge_num += 1

        # all edges found
        if found_edge_num == n - 1:
            break

print(sum(i[2] for i in edges) - weight)

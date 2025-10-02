a = {(1, (5,)): 1.0}

for _ in range(16):
    b = {}
    for k in a:
        n, state = k
        l = len(state)
        for paper_ind in range(len(state)):
            new_state = state[:paper_ind] + state[paper_ind + 1 :]
            paper_to_cut = state[paper_ind]
            new_state += tuple(range(1, paper_to_cut))
            new_k = n + (len(new_state) == 1), new_state
            if new_k not in b:
                b[new_k] = 0
            b[new_k] += a[k] / l
    a = b

v = sum(k[0] * a[k] for k in a) - 2
print(round(v, 6))

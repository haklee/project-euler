d = {}
i = 0
while i < 10**4:
    s = "".join(sorted(str(i**3)))
    if s in d:
        d[s].append(i)
    else:
        d[s] = [i]
    i += 1

print(min(d[i] for i in d if len(d[i]) == 5)[0] ** 3)

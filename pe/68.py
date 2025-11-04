numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]

sol = []

from itertools import permutations

for candidate in permutations(numbers):
    o1, o2, o3, o4, o5, i1, i2, i3, i4, i5 = [10, *candidate]
    if (
        len(set([o1 + i1 + i2, o2 + i2 + i3, o3 + i3 + i4, o4 + i4 + i5, o5 + i5 + i1]))
        == 1
    ):
        x = [o1, i1, i2, o2, i2, i3, o3, i3, i4, o4, i4, i5, o5, i5, i1] * 2
        sol.append(min(x[i : i + 15] for i in range(0, 15, 3)))

print("".join(str(i) for i in max(sol)))

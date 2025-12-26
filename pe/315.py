# 7-segment index:
#
# ┌ 1 ┐
# 2   3
# ├ 4 ┤
# 5   6
# └ 7 ┘

digit_list = " 0123456789"

segment = {
    " ": set(),
    "0": {1, 2, 3, 5, 6, 7},
    "1": {3, 6},
    "2": {1, 3, 4, 5, 7},
    "3": {1, 3, 4, 6, 7},
    "4": {2, 3, 4, 6},
    "5": {1, 2, 4, 6, 7},
    "6": {1, 2, 4, 5, 6, 7},
    "7": {1, 2, 3, 6},
    "8": {1, 2, 3, 4, 5, 6, 7},
    "9": {1, 2, 3, 4, 6, 7},
}

transition = {
    i: {j: len(segment[j].symmetric_difference(segment[i])) for j in digit_list}
    for i in digit_list
}

from sympy import primerange

num_array = primerange(10**7, 2 * 10**7)
# num_array=[137]
total_len = 8
sol = 0

for num in num_array:
    sam_cnt = max_cnt = 0
    cur, next = " " * total_len, str(num)
    while True:
        max_cnt += sum(
            transition[i][j]
            for i, j in zip(cur.rjust(total_len, " "), next.rjust(total_len, " "))
        )
        sam_cnt += sum(
            transition[i][j] for i, j in zip(cur.rjust(total_len, " "), " " * total_len)
        )
        sam_cnt += sum(
            transition[i][j]
            for i, j in zip(" " * total_len, next.rjust(total_len, " "))
        )

        cur, next = next, str(sum(map(int, next)))
        if cur == next:
            break
    sol += sam_cnt - max_cnt

print(sol)

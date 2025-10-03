n = 10**2  # < change this value!
evens = {"0", "2", "4", "6", "8"}
sol = 0
for i in range(1, n):
    if i % 10 == 0:
        continue
    v = i + int("".join(str(i)[::-1]))
    if len(set(str(v)).intersection(evens)) == 0:
        sol += 1
print(sol)

print(
    sum(
        [
            0,
            20,
            100,
            600,
            0,
            18000,
            50000,
            540000,
            0,
        ]
    )
)

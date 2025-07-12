print(
    max(
        i * j
        for i in range(100, 1000)
        for j in range(100, i + 1)
        if (s := str(i * j)) == "".join(reversed(s))
    )
)

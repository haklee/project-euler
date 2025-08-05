print(
    len(set(i**j for i in range(1, 10) for j in range(1, 100) if len(str(i**j)) == j))
)

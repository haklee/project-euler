print(sum(i for i in range(10, 10**6) if sum(j**5 for j in map(int, str(i))) == i))

def int_tri(n):
    cnt = 0
    for i in range(1, n // 2 + 1):
        m = n - i
        for j in range(m // 2, m):
            cnt += (i * j * (m - j) != 0) and (j**2 + (m - j) ** 2 == i**2)
    return cnt


print(max([(int_tri(i), i) for i in range(1, 1001)])[1])

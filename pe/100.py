def f(n):
    return int(n / 2**0.5) + 1


n = 1
x = 1
while 1:
    m = f(n)
    if m * (m - 1) * 2 == n * (n - 1):
        p = n / x
        print(
            f"(blue:{m}), (total:{n}), (cur_total / prev_total:{p}), (next_total_prediction:{int(n*p)})"
        )
        if n > 10**12:
            break
        x = n
        n = int(n * p)
    n += 1

print(m)

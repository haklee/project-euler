n = 10**16
sol = 0

# start from 4, since 3*3 is only one digit and can't be split into more than two numbers.
for i in range(4, int(n**0.5) + 1):
    if i % 9 not in [0, 1]:
        continue
    number_string = str(i * i)
    for j in range(len(number_string) - 1):
        x, y = number_string[: j + 1], number_string[j + 1 :]
        if y[0] != "0" and int(x) + int(y) == i:
            sol += i * i
            print(i * i)
            break
print(sol)

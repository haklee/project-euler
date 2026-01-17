from itertools import product

n = 10**12
sol = 0

# start from 4, since 3*3 is only one digit and can't be split into more than two numbers.
for i in range(4, int(n**0.5) + 1):
    if i % 9 not in [0, 1]:
        # cutting:
        # any split digit sum is equal to all digit sum modulo 9.
        # for example, 1+23+456 == 1+2+3+4+5+6 (mod 9).
        # so, i*i == i (mod 9) holds, and this holds if i%9 is 1 or 0.
        continue
    number_string = str(i * i)
    insert_plus = product(*[[0, 1] for _ in range(len(number_string) - 1)])
    for x in insert_plus:
        numbers = []
        cur_num = number_string[0]
        for j in range(len(x)):
            if x[j] == 1:
                numbers.append(int(cur_num))
                cur_num = ""
            cur_num += number_string[j + 1]
        numbers.append(int(cur_num))

        if sum(numbers) == i:
            sol += i * i
            print(i * i)
            break
print(sol)

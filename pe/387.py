from sympy import isprime

num_digits = 14

right_harshad_numbers = range(1, 10)
iter = 0
sol = 0
while iter < num_digits - 2:
    iter += 1
    tmp = []
    for n in right_harshad_numbers:
        for i in range(10):
            new_num_str = str(n) + str(i)
            if int(new_num_str) % sum(int(d) for d in new_num_str) == 0:
                tmp.append(int(new_num_str))
                if isprime(int(new_num_str) // sum(int(d) for d in new_num_str)):
                    # strong right harshad number.
                    # check if concatenating a number at the end makes prime.
                    for p in [1, 3, 7, 9]:
                        sol_cand = str(new_num_str) + str(p)
                        if isprime(int(sol_cand)):
                            print(sol_cand)
                            sol += int(sol_cand)
    right_harshad_numbers = tmp

print(sol)

a=10**17
b=9**17

diff_bin = bin(a-b)[2:]
sol = a

for i in range(len(diff_bin)-1, -1, -1):
    v = (a-int(diff_bin[i:], 2))*int(diff_bin[i])
    sol += v

print(sol)
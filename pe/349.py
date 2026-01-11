pos = (0, 0)
dir = (1, 0)
black = set()
target = 10**18

iter = 100000
black_num = [0]

# get black_num values
for i in range(iter):
    if pos in black:
        black.remove(pos)
        dir = (-dir[1], dir[0])
        pos = (pos[0] + dir[0], pos[1] + dir[1])
    else:
        black.add(pos)
        dir = (dir[1], -dir[0])
        pos = (pos[0] + dir[0], pos[1] + dir[1])
    black_num.append(len(black))

# find loop length
loop_len = 1
test_lim = 1000
while loop_len < test_lim:
    loop_test = black_num[-10 * test_lim :: loop_len]
    if len(set(i - j for i, j in zip(loop_test[:-1], loop_test[1:]))) == 1:
        break
    loop_len += 1


base = iter - 10 * test_lim
base += (target % loop_len) - (base % loop_len)
loop_num = black_num[base + loop_len] - black_num[base]
print(black_num[base] + ((target - base) // loop_len) * loop_num)

a = [s[1:-1] for s in input().split(",")]

d = {}

for s in a:
    k = "".join(sorted(s))
    if not k in d:
        d[k] = []
    d[k].append(s)

d = {k: d[k] for k in d if len(d[k]) > 1}

key_list = sorted([k for k in d], key=lambda i: -len(i))
longest_length = len(key_list[0])
squares = {}
i = 1
while 1:
    k = len(str(i * i))
    if k > longest_length:
        break
    if k not in squares:
        squares[k] = []
    squares[k].append(str(i * i))
    i += 1

candidate = []

for k in d:
    length = len(k)
    square_list = squares[length]

    first_word = d[k][0]
    print(first_word)

    for sq in square_list:
        # init map
        map_info = {c: [] for c in first_word}
        for i in range(length):
            map_info[first_word[i]].append(sq[i])

        # if map not valid, break.
        # for example, 123 can not map to SEE.
        if any(len(i) != 1 for i in map_info.values()):
            continue

        # map char to char
        # for example, if 122 map to SEE,
        # then, map_info = {'S':'1', 'E':'2'}
        map_info = {k: map_info[k][0] for k in map_info}

        # check for invalid case like
        # 111 map to SEE.
        if len(set(map_info.values())) != len(map_info.keys()):
            continue

        # check for other words in anagram set.
        mapped_numbers = []
        for word in d[k]:
            num = "".join([map_info[c] for c in word])
            mapped_numbers.append(num)

        if all(num in square_list for num in mapped_numbers):
            print(d[k], mapped_numbers)
            candidate += mapped_numbers

print(sorted([int(i) for i in candidate])[::-1])

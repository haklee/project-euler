from sympy import primerange

n = 10**8
words = [bin(i)[2:][::-1] for i in primerange(n)]
trie = {"children": [None, None], "leaf_cnt": [0, 0]}
for word in words:
    cur_node = trie
    for char in word:
        num = int(char)
        if cur_node["children"][num] == None:
            cur_node["children"][num] = {"children": [None, None], "leaf_cnt": [0, 0]}
        cur_node["leaf_cnt"][num] += 1
        cur_node = cur_node["children"][num]

sol = 0


def count_max(node):
    global sol
    sol += max(node["leaf_cnt"])
    for child in node["children"]:
        if child:
            count_max(child)


count_max(trie)

print(sol / len(words))

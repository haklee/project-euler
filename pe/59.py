from collections import Counter

s = input().split(",")
a = [*enumerate(map(int, s))]
a0 = Counter([i[1] for i in a if i[0] % 3 == 0])
a1 = Counter([i[1] for i in a if i[0] % 3 == 1])
a2 = Counter([i[1] for i in a if i[0] % 3 == 2])

secret_key = (
    chr(a0.most_common(1)[0][0] ^ ord(" "))
    + chr(a1.most_common(1)[0][0] ^ ord(" "))
    + chr(a2.most_common(1)[0][0] ^ ord(" "))
)
text = [int(i[1]) ^ ord(secret_key[i[0] % 3]) for i in enumerate(s)]

print(sum(text))

# run like:
# $ python 79.py < 79.data

import re

a = sorted(list([i.replace("\n", "") for i in open(0)]))
s = list("".join(a))
for i in range(len(s)):
    t = list(s)
    t[i] = "x"
    for p in a:
        r = re.findall(f".*{p[0]}.*{p[1]}.*{p[2]}.*", "".join(t))
        if not r:
            break
    else:
        s = t

print("".join([i for i in s if i != "x"]))

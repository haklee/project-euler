# run like:
# $ python 102.py < 102.data

def check_containment(x1, y1, x2, y2, x3, y3):
    o1 = x1 * (y2 - y1) - (x2 - x1) * y1
    o2 = x2 * (y3 - y2) - (x3 - x2) * y2
    o3 = x3 * (y1 - y3) - (x1 - x3) * y3
    return all(i > 0 for i in [o1, o2, o3]) or all(i < 0 for i in [o1, o2, o3])


print(sum(check_containment(*map(int, l.split(","))) for l in open(0)))

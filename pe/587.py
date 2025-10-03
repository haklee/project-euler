from math import pi, asin

area_l = 1 - pi / 4


def area_tri(n):
    upper_tri = (n - 1) * (1 + n - (2 * n) ** 0.5) / 2 / (1 + n**2)
    cut_circle = asin(1 - n * (1 + n - (2 * n) ** 0.5) / (1 + n**2)) / 2
    return 1 / 2 - upper_tri - cut_circle


l, h = 0, 5000
while l < h:
    m = (l + h) // 2
    if area_tri(m) / area_l > 0.001:
        l = m + 1
    else:
        h = m

print(l)

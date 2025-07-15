a = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
b = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
c = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

# last two digits
x = sum(len(i) for i in a) * 9 + sum(len(i) for i in b) + sum(len(i) for i in c) * 10

# (x) hundred and ... <- x appears 100 times.
y1 = sum(len(i) for i in a) * 100

# x (hundred) and ... <- 'hundred' appears 100 * 9 times.
y2 = len("hundred") * 100 * 9

# x hundred (and) ... <- 'and' appears when last two digit is not '00'.
y3 = len("and") * 99 * 9

# one thousand
z = len("onethousand")

print(x + y1 + y2 + y3 + z)

# run like:
# $ python 54.py < 54.data


ORDER = {
    "high": 0,
    "pair": 1,
    "two_pairs": 2,
    "three": 3,
    "straight": 4,
    "flush": 5,
    "full_house": 6,
    "four": 7,
    "straight_flush": 8,
    "royal_flush": 9,
}

FAIL = (-1, -1, [-1])

# scores are in format: (rank order, representing card of rank, cards in descending order)


def high(cards):
    number_list = sorted([i[0] for i in cards], key=lambda x: -x)
    return (ORDER["high"], 0, number_list)


def pair(cards):
    number_list = sorted([i[0] for i in cards], key=lambda x: -x)
    for i in number_list:
        if number_list.count(i) == 2:
            return (ORDER["pair"], i, number_list)
    return FAIL


def two_pairs(cards):
    number_list = sorted([i[0] for i in cards], key=lambda x: -x)
    x = []
    for i in set(number_list):
        if number_list.count(i) == 2:
            x.append(i)

    if len(x) == 2:
        # Description unclear:
        # What if (3,3,2,2,9) vs (1,1,2,2,9)?
        # It seems test cases are not affected by this.
        return (ORDER["two_pairs"], -1, number_list)
    else:
        return FAIL


def three_of_a_kind(cards):
    number_list = sorted([i[0] for i in cards], key=lambda x: -x)

    for i in number_list:
        if number_list.count(i) == 3:
            return (ORDER["three"], i, number_list)
    return FAIL


def full_house(cards):
    number_list = sorted([i[0] for i in cards], key=lambda x: -x)

    if pair(cards) != FAIL and three_of_a_kind(cards) != FAIL:
        # Description unclear:
        # What if (3,3,3,2,2) vs (3,3,3,1,1)?
        # It seems test cases are not affected by this.
        return (ORDER["full_house"], -1, number_list)

    return FAIL


def four_of_a_kind(cards):
    number_list = sorted([i[0] for i in cards], key=lambda x: -x)

    for i in number_list:
        if number_list.count(i) == 4:
            return (ORDER["four"], i, number_list)
    return FAIL


def straight(cards):
    number_list = sorted([i[0] for i in cards], key=lambda x: -x)
    if all(
        i == j
        for i, j in zip(
            number_list[::-1], range(min(number_list), min(number_list) + 5)
        )
    ):
        return (ORDER["straight"], max(number_list), number_list)
    return FAIL


def flush(cards):
    number_list = sorted([i[0] for i in cards], key=lambda x: -x)
    suit_list = [i[1] for i in cards]
    if len(set(suit_list)) == 1:
        return (ORDER["flush"], 0, number_list)
    return FAIL


def straight_flush(cards):
    number_list = sorted([i[0] for i in cards], key=lambda x: -x)
    if straight(cards) != FAIL and flush(cards) != FAIL:
        return (ORDER["straight_flush"], 0, number_list)
    return FAIL


def royal_flush(cards):
    number_list = sorted([i[0] for i in cards], key=lambda x: -x)
    if straight_flush(cards) != FAIL and number_list[-1] == 14:
        return (ORDER["royal_flush"], 0, number_list)
    return FAIL


def hand(cards):
    res = max(
        royal_flush(cards),
        straight_flush(cards),
        flush(cards),
        straight(cards),
        four_of_a_kind(cards),
        full_house(cards),
        three_of_a_kind(cards),
        two_pairs(cards),
        pair(cards),
        high(cards),
    )
    return res


sol = 0

for s in open(0):
    cards = (
        s.replace("T", "10")
        .replace("J", "11")
        .replace("Q", "12")
        .replace("K", "13")
        .replace("A", "14")
        .split()
    )
    cards = [(int(i[:-1]), i[-1]) for i in cards]
    sol += hand(cards[:5]) > hand(cards[5:])

print(sol)

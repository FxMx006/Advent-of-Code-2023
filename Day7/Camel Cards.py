def rank_hand(hand):
    order = '23456789TJQKA'
    counts = {i: hand.count(i) for i in hand}
    keys = sorted(counts, key=lambda x:(counts[x], order.index(x)), reverse=True)
    if len(keys) == 5:
        return [1] + [order.index(i) for i in hand]
    if len(keys) == 4:
        return [2] + [order.index(i) for i in hand]
    if len(keys) == 3:
        if 3 in counts.values():
            return [4] + [order.index(i) for i in hand]
        else:
            return [3] + [order.index(i) for i in hand]
    if len(keys) == 2:
        if 4 in counts.values():
            return [6] + [order.index(i) for i in hand]
        else:
            return [5] + [order.index(i) for i in hand]
    return [7] + [order.index(i) for i in hand]


def camel_cards(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    hands = [(line.split()[0], int(line.split()[1])) for line in lines]
    hands = sorted(hands, key=lambda x: rank_hand(x[0]))
    total_winnings = sum(hand[1] * (i+1) for i, hand in enumerate(hands))
    return total_winnings


print(camel_cards("Input.txt"))

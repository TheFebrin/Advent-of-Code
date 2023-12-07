from collections import Counter
from functools import cmp_to_key

def get_poker_hand_score(counter: Counter) -> int:
    """
    High card: 0
    One pair: 1
    Two pairs: 2
    Three of a kind: 3
    Full house: 4
    Four of a kind: 5
    Five of a kind: 6
    """
    if len(counter) == 5:
        return 0
    elif len(counter) == 4:
        return 1
    elif len(counter) == 3:
        if 3 in counter.values():
            return 3
        else:
            return 2
    elif len(counter) == 2:
        if 3 in counter.values():
            return 4
        else:
            return 5
    elif len(counter) == 1:
        return 6

card_to_value = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

def solve(data):

    @cmp_to_key
    def __sort(x, y):
        hand, cash, score = x
        hand2, cash2, score2 = y

        if score != score2:
            return 1 if score > score2 else -1
        else:
            for i in range(len(hand)):
                if hand[i] != hand2[i]:
                    v1, v2 = card_to_value[hand[i]], card_to_value[hand2[i]]
                    return 1 if v1 > v2 else -1

    scores = []
    for x in data:
        hand, cash = x.split()
        counter = Counter(hand)
        scores.append((hand, cash, get_poker_hand_score(counter)))

    scores.sort(key=__sort, reverse=False)

    ans = 0
    for i, x in enumerate(scores):
        ans += int(x[1]) * (i + 1)
    print(ans)


"""
Part 2
"""

card_to_value2 = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 12,
    "K": 13,
    "A": 14
}

def get_poker_hand_score2(counter: Counter) -> int:
    """
    High card: 0
    One pair: 1
    Two pairs: 2
    Three of a kind: 3
    Full house: 4
    Four of a kind: 5
    Five of a kind: 6
    """
    n_jokers = counter["J"]
    del counter["J"]

    max_cnt, max_card = 0, None
    for k, v in counter.items():
        if v > max_cnt:
            max_cnt, max_card = v, k

    counter[max_card] += n_jokers

    if len(counter) == 5:
        return 0
    elif len(counter) == 4:
        return 1
    elif len(counter) == 3:
        if 3 in counter.values():
            return 3
        else:
            return 2
    elif len(counter) == 2:
        if 3 in counter.values():
            return 4
        else:
            return 5
    elif len(counter) == 1:
        return 6


def solve2(data):

    @cmp_to_key
    def __sort(x, y):
        hand, cash, score = x
        hand2, cash2, score2 = y

        if score != score2:
            return 1 if score > score2 else -1
        else:
            for i in range(len(hand)):
                if hand[i] != hand2[i]:
                    v1, v2 = card_to_value2[hand[i]], card_to_value2[hand2[i]]
                    return 1 if v1 > v2 else -1

    scores = []
    for x in data:
        hand, cash = x.split()
        counter = Counter(hand)
        scores.append((hand, cash, get_poker_hand_score2(counter)))

    scores.sort(key=__sort, reverse=False)

    ans = 0
    for i, x in enumerate(scores):
        ans += int(x[1]) * (i + 1)
        # print(x)
    print(ans)


def main():
    with open("data.txt") as f:
        data = f.read().splitlines()
        solve2(data)

if __name__ == "__main__":
    main()
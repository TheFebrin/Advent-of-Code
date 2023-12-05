
def solve(data):
    """
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    """
    ans = 0
    for row in data:
        score = 1
        row = row.split(" | ")
        winning = row[0][row[0].index(":") + 2:].split(" ")
        my = row[1].split()
        for x in my:
            if x in winning:
                score *= 2
        ans += score // 2
    print(ans)


def solve2(data):
    cards = {i: 1 for i in range(1, len(data) + 1)}
    for i, row in enumerate(data):
        card_n = i + 2
        row = row.split(" | ")
        winning = row[0][row[0].index(":") + 2:].split(" ")
        my = row[1].split()
        for x in my:
            if x in winning:
                cards[card_n] += cards[i + 1]
                card_n += 1

    print(sum(cards.values()))

def main():
    with open("data.txt") as f:
        data = f.read().splitlines()
        solve2(data)

if __name__ == "__main__":
    main()
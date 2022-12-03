from typing import *

def solve1() -> None:
    rules = {
        "A": {"X": 3+1, "Y": 6+2, "Z": 0+3},
        "B": {"X": 0+1, "Y": 3+2, "Z": 6+3},
        "C": {"X": 6+1, "Y": 0+2, "Z": 3+3},
    }
    ans = 0
    with open("data.txt") as f:
        for line in f.readlines():
            opp, me = line.split()
            ans += rules[opp][me]
    print(ans)


def solve2() -> None:
    """
    X - lose
    Y - draw
    Z - win
    """
    rules = {
        "A": {"X": 3+1, "Y": 6+2, "Z": 0+3},
        "B": {"X": 0+1, "Y": 3+2, "Z": 6+3},
        "C": {"X": 6+1, "Y": 0+2, "Z": 3+3},
    }
    adapt_choice = {
        "A": {"X": "Z", "Y": "X", "Z": "Y"},
        "B": {"X": "X", "Y": "Y", "Z": "Z"},
        "C": {"X": "Y", "Y": "Z", "Z": "X"},
    }
    ans = 0
    with open("data.txt") as f:
        for line in f.readlines():
            opp, me = line.split()
            me = adapt_choice[opp][me]
            ans += rules[opp][me]
    print(ans)


def main() -> None:
    solve2()

if __name__ == __name__:
    main()
from typing import *

def solve1() -> None:
    ans = 0
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.strip()
            l, r = line[:len(line) // 2], line[len(line) // 2:]
            inter = set(l).intersection(set(r))
            for x in inter:
                if x.islower():
                    ans += ord(x) - ord('a') + 1
                else:
                    ans += ord(x) - ord('A') + 27
    print(ans)


def solve2() -> None:
    ans = 0
    data = []
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line)

    for i in range(0, len(data), 3):
        line1, line2, line3 = data[i], data[i + 1], data[i + 2]
        inter = set(line1).intersection(set(line2))
        inter = inter.intersection(set(line3))
        for x in inter:
            if x.islower():
                ans += ord(x) - ord('a') + 1
            else:
                ans += ord(x) - ord('A') + 27
    print(ans)


def main() -> None:
    solve2()

if __name__ == __name__:
    main()
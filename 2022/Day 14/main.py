
from typing import *


def can_drop(cave: List[List[str]], x: int, y: int) -> Tuple[bool, bool, bool]:
    drop_down = cave[x + 1][y] == "."
    drop_left = y - 1 >= 0 and cave[x + 1][y - 1] == "."
    drop_right = cave[x + 1][y + 1] == "."
    return drop_down, drop_left, drop_right


def simmulate(cave: List[List[str]]) -> Optional[bool]:
    x, y = 0, 500

    if sum(can_drop(cave=cave, x=x, y=y)) == 0:
        return True

    while True:
        drop_down, drop_left, drop_right = can_drop(cave=cave, x=x, y=y)
        if sum((drop_down, drop_left, drop_right)) == 0:
            break

        if drop_down:
            x += 1
        elif drop_left:
            x += 1
            y -= 1
        elif drop_right:
            x += 1
            y += 1
        
        if x == len(cave) - 1:
            return True

    cave[x][y] = "o"


def show_cave(cave: List[List[str]]) -> None:
    for row in cave[:15]:
        print(row[494:505])


def solve1() -> None:
    W, H = 1000, 1000
    cave = [
        ['.' for j in range(W)]
        for i in range(H)
    ]
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.strip()
            line = line.split(" -> ")
            for i in range(len(line) - 1):
                y, x = map(int, line[i].split(','))
                next_y, next_x = map(int, line[i + 1].split(','))
                if x == next_x:
                    for k in range(min(y, next_y), max(y, next_y) + 1):
                        cave[x][k] = "#"
                elif y == next_y:
                    for k in range(min(x, next_x), max(x, next_x) + 1):
                        cave[k][y] = "#"
                else:
                    raise RuntimeError()

    cave[0][500] = "+"
    for i in range(1000):
        end = simmulate(cave=cave)
        if end:
            print(i)
            break

def solve2() -> None:
    W, H = 1000, 1000
    cave = [
        ['.' for j in range(W)]
        for i in range(H)
    ]
    floor_level = 0
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.strip()
            line = line.split(" -> ")
            for i in range(len(line) - 1):
                y, x = map(int, line[i].split(','))
                next_y, next_x = map(int, line[i + 1].split(','))
                floor_level = max(floor_level, x)
                floor_level = max(floor_level, next_x)
                if x == next_x:
                    for k in range(min(y, next_y), max(y, next_y) + 1):
                        cave[x][k] = "#"
                elif y == next_y:
                    for k in range(min(x, next_x), max(x, next_x) + 1):
                        cave[k][y] = "#"
                else:
                    raise RuntimeError()

    print(floor_level)
    for j in range(W):
        cave[floor_level + 2][j] = "#"

    cave[0][500] = "+"
    for i in range(1000000):
        end = simmulate(cave=cave)
        # show_cave(cave=cave)
        if end:
            print("end: ", i + 1)
            break

def main() -> None:
    solve2()

if __name__ == '__main__':
    main()


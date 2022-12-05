from typing import *

def solve1() -> None:
    ans = 0
    with open("data.txt") as f:
        for line in f.readlines():
            l, r = line.split(",")
            ll, lr = map(int, l.split('-'))
            rl, rr = map(int, r.split('-'))
            
            if ll <= rl <= rr <= lr or rl <= ll <= lr <= rr:
                ans += 1
                
    print(ans)
            


def solve2() -> None:
    ans = 0
    with open("data.txt") as f:
        for line in f.readlines():
            l, r = line.split(",")
            ll, lr = map(int, l.split('-'))
            rl, rr = map(int, r.split('-'))
            
            if ll <= rl <= lr or ll <= rr <= lr\
                or rl <= ll <= rr or rl <= lr <= rr:
                ans += 1
                
    print(ans)


def main() -> None:
    solve2()

if __name__ == __name__:
    main()
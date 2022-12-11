from typing import *

def solve1() -> None:
    ans = 0
    vals = [0] * 100000
    vals[0] = 1
    cycle = 1
    important_cycles = [20, 60, 100, 140, 180, 220]
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.strip()
            vals[cycle] += vals[cycle - 1]
            if cycle in important_cycles:
                print(f"cycle: {cycle} => {vals[cycle]}")
                ans += cycle * vals[cycle]
                # print(vals[:cycle+2])
            if line == "noop":
                pass
            else:
                opp, val = line.split()
                vals[cycle + 2] += int(val) 
                cycle += 1
                vals[cycle] += vals[cycle - 1]
                if cycle in important_cycles:
                    print(f"cycle: {cycle} => {vals[cycle]}")
                    ans += cycle * vals[cycle]
                # print(f"Adding {int(val)} to {cycle + 1}")
            cycle += 1

    print('Ended on cycle: ', cycle)
    for i in range(20):
        if cycle in important_cycles:
            print(f"cycle: {cycle} => {vals[cycle]}")
        vals[cycle] += vals[cycle - 1]
        cycle += 1


    print('ans: ', ans)


def solve2() -> None:
    ans = 0
    vals = [0] * 100000
    vals[0] = 1
    cycle = 1

    board = [
        ["." for i in range(40)]
        for j in range(6)
    ]
   
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.strip()
            vals[cycle] += vals[cycle - 1]

            tmp_cycle = cycle - 1
            position = tmp_cycle % 40
            if abs(position - vals[cycle]) <= 1:
                board[tmp_cycle // 40][tmp_cycle % 40] = '#'

            if line == "noop":
                pass
            else:
                opp, val = line.split()
                vals[cycle + 2] += int(val) 
                cycle += 1
                vals[cycle] += vals[cycle - 1]
                
                tmp_cycle = cycle - 1
                position = tmp_cycle % 40
                if abs(position - vals[cycle]) <= 1:
                    board[tmp_cycle // 40][tmp_cycle % 40] = '#'
                
            cycle += 1

    for row in board:
        print(*row)

def main() -> None:
    solve2()

if __name__ == __name__:
    main()
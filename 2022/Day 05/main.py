from typing import *

def solve1() -> None:
    data = [
        list("      RJW"),
        list("   RN TTC"),
        list("R  PG JPT"),
        list("Q CMV FFH"),
        list("GPMSZ ZCQ"),
        list("PCPQJJPHZ"),
        list("CTHTHPGLV"),
        list("FWBLPDLNG"),
    ]
    stacks = [
        [
            data[i][j] 
            for i in reversed(range(len(data)))
            if data[i][j] != " "
        ]
        for j in range(len(data[0]))
    ]        
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.split()
            action, how_many, _, num_from, _, num_to = line
            how_many, num_from, num_to = map(int, [how_many, num_from, num_to])
            
            for _ in range(how_many):
                x = stacks[num_from - 1].pop()
                stacks[num_to - 1].append(x)

    print("".join([x[-1] for x in stacks]))


def solve2() -> None:
    data = [
        list("      RJW"),
        list("   RN TTC"),
        list("R  PG JPT"),
        list("Q CMV FFH"),
        list("GPMSZ ZCQ"),
        list("PCPQJJPHZ"),
        list("CTHTHPGLV"),
        list("FWBLPDLNG"),
    ]
    stacks = [
        [
            data[i][j] 
            for i in reversed(range(len(data)))
            if data[i][j] != " "
        ]
        for j in range(len(data[0]))
    ]        
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.split()
            action, how_many, _, num_from, _, num_to = line
            how_many, num_from, num_to = map(int, [how_many, num_from, num_to])
            
            to_insert = []
            for _ in range(how_many):
                x = stacks[num_from - 1].pop()
                to_insert.append(x)
            
            for x in reversed(to_insert):
                stacks[num_to - 1].append(x)

    print("".join([x[-1] for x in stacks]))


def main() -> None:
    solve2()

if __name__ == __name__:
    main()
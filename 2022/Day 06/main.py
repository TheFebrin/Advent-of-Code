from typing import *

def solve1() -> None:
     with open("data.txt") as f:
        data = f.readline()
        for i in range(len(data) - 14):
            if len(set(data[i:i+14])) == 14:
                print(i + 14, data[i:i+14])
                break



def main() -> None:
    solve1()

if __name__ == __name__:
    main()
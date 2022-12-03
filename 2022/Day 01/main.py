from typing import *


def main() -> None:
    ans = []
    with open("data.txt") as f:
        one_elf_calories = 0
        for line in f.readlines():
            if len(line) == 1:
                ans.append(one_elf_calories)
                one_elf_calories = 0
            else:
                one_elf_calories += int(line.strip())

    print(sorted(ans, reverse=True)[:3])
    print(sum(sorted(ans, reverse=True)[:3]))


if __name__ == __name__:
    main()
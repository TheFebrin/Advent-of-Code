import os

template: str = """
from typing import *

def solve1() -> None:
    ...

def solve2() -> None:
    ...

def main() -> None:
    solve1()

if __name__ == '__main__':
    main()

"""

def main() -> None:
    for i in range(1, 26):
        os.mkdir(f"Day {i}")

        with open (f"Day {i}/main.py", "w") as f:
            f.write(template)

        with open (f"Day {i}/data.txt", "w") as f:
            f.write("Hello")


if __name__ == '__main__':
    main()
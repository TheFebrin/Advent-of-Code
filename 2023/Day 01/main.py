
digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def is_number(x: str, i: int) -> str:
    for d in digits:
        if x[i: i + len(d)] == d:
            return str(digits.index(d) + 1)

        if x[i].isdigit():
            return x[i]

def solve2(x: str) -> int:
    d1 = [is_number(x, i) for i in range(len(x))]
    d1 = [x for x in d1 if x is not None][0]
    d2 = [is_number(x, i) for i in reversed(range(len(x)))]
    d2 = [x for x in d2 if x is not None][0]
    return int(d1 + d2)


def solve(x: str) -> int:
    nums = [it for it in x if it.isdigit()]
    if len(nums) == 1:
        return int(nums[0] + nums[0])
    return int(nums[0] + nums[-1])


def main():
    with open("data.txt") as f:
        data = f.read().splitlines()
        ans = 0
        for x in data:
            ans += solve2(x)
        print(ans)

if __name__ == "__main__":
    main()
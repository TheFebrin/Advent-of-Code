
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
def solve(x: str) -> int:
    nums = [it for it in x if it.isdigit()]
    if len(nums) == 1:
        return int(nums[0] + nums[0])
    return int(nums[0] + nums[-1])


def get_digit(x: str) -> str:
    for i in range(len(x)):
        for d in digits:
            if x[i: i + len(d)] == d:
                return str(digits.index(d) + 1)

            if x[i].isdigit():
                return x[i]

def get_digit_rev(x: str) -> str:
    for i in reversed(range(len(x))):
        for d in digits:
            if x[i: i + len(d)] == d:
                return str(digits.index(d) + 1)

            if x[i].isdigit():
                return x[i]

def solve2(x: str) -> int:
    d1 = get_digit(x)
    d2 = get_digit_rev(x)
    return int(d1 + d2)

def main():
    with open("data.txt") as f:
        data = f.read().splitlines()
        ans = 0
        for x in data:
            ans += solve2(x)
        print(ans)

if __name__ == "__main__":
    main()
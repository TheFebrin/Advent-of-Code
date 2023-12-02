
possible = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def solve2(x) -> bool:
    """
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    """
    x = x[x.find(":") + 2:]
    x = x.split(";")
    x = [x.split(", ") for x in x]

    min_red = 0
    min_green = 0
    min_blue = 0
    for game in x:
        for item in game:
            count, color = item.strip().split(" ")
            count = int(count)
            if color == "red":
                min_red = max(min_red, count)
            elif color == "green":
                min_green = max(min_green, count)
            elif color == "blue":
                min_blue = max(min_blue, count)

    return min_red * min_green * min_blue


def solve(x) -> bool:
    """
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    """
    x = x[x.find(":") + 2:]
    x = x.split(";")
    x = [x.split(", ") for x in x]

    for game in x:
        for item in game:
            count, color = item.strip().split(" ")
            count = int(count)
            if count > possible[color]:
                return False
    return True

def main():
    with open("data.txt") as f:
        data = f.read().splitlines()
        ans = 0
        for i, x in enumerate(data):
            ans += solve2(x)
        print(ans)

if __name__ == "__main__":
    main()
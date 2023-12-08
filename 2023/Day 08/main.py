import itertools
from functools import reduce


def solve(data):
    sequence = data[0]
    map = {}

    for x in data[2:]:
        x = x.split()

        start = x[0]
        dest_l = x[2].replace("(", "").replace(",", "")
        dest_r = x[3].replace(")", "")

        map[start] = (dest_l, dest_r)

    act = "AAA"
    ans = 0
    for x in itertools.cycle(sequence):
        act = map[act][0] if x == "L" else map[act][1]
        ans += 1
        if act == "ZZZ":
            break

    print(ans)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve2(data):
    sequence = data[0]
    map = {}

    for x in data[2:]:
        x = x.split()

        start = x[0]
        dest_l = x[2].replace("(", "").replace(",", "")
        dest_r = x[3].replace(")", "")

        map[start] = (dest_l, dest_r)

    act = []
    for x in map.keys():
        if x.endswith("A"):
            act.append(x)


    all_ans = []
    for a in act:
        ans = 0
        for x in itertools.cycle(sequence):
            a = map[a][0] if x == "L" else map[a][1]
            ans += 1
            if a.endswith("Z"):
                all_ans.append(ans)
                break

    print(all_ans)
    gcd_all = reduce(gcd, all_ans)
    final_ans = reduce(lambda x, y: x * y / gcd(x, y), all_ans)
    print(final_ans)

def main():
    with open("data.txt") as f:
        data = f.read().splitlines()
        solve2(data)

if __name__ == "__main__":
    main()
import numpy as np


def solve(data):
    ans = 0
    for x in data:
        x = [int(x) for x in x.split()]
        all_diffs = [np.array(list(reversed(x)))]
        while not all([x == all_diffs[-1][0] for x in all_diffs[-1]]):
            all_diffs.append(np.diff(np.array(all_diffs[-1]), 1))

        for i in reversed(range(1, len(all_diffs))):
            all_diffs[i - 1] = all_diffs[i - 1].tolist()
            all_diffs[i - 1].append(all_diffs[i - 1][-1] + all_diffs[i][-1])

        # for x in all_diffs:
        #     print(x)
        # print("===")
        ans += all_diffs[0][-1]
    print(ans)

def main():
    with open("data.txt") as f:
        data = f.read().splitlines()
        solve(data)

if __name__ == "__main__":
    main()
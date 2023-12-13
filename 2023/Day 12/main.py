import time
from copy import copy
from functools import cache

from tqdm import tqdm


def generate(nums, length):
    ans = []

    def rec(act_pose, idx, act_arr):
        if idx == len(nums):
            ans.append(act_arr)
            return

        for i in range(act_pose, length - nums[idx] + 1):
            arr = copy(act_arr)
            for j in range(i, i + nums[idx]):
                arr[j] = "#"
            rec(i + nums[idx] + 1, idx + 1, arr)

    rec(0, 0, ["."] * length)
    return ans


def solve(data):
    s = 0
    for x in data:
        x = x.split()
        nums = [int(it) for it in x[1].split(",")]

        g = generate(nums=nums, length=len(x[0]))
        ans = 0

        for a in g:
            good = True
            for i in range(len(a)):
                if (a[i] == "#" and x[0][i] == '.') or (x[0][i] == '#' and a[i] != '#'):
                    good = False
                    break
            if good:
                ans += 1

        # print(ans)
        s += ans
    print(s)


def generate2(nums: list[int], og_boi):
    @cache
    def solve_rec(og_boi, idx):
        if idx == len(nums):
            return og_boi.count("#") == 0

        if len(og_boi) < sum(nums[idx:]):
            return 0

        ans = 0
        can_put_all_hashes = og_boi[:nums[idx]].count('.') == 0
        can_put_dot_after = len(og_boi) == nums[idx] or og_boi[nums[idx]] != '#'
        if can_put_all_hashes and can_put_dot_after:
            ans += solve_rec(og_boi=og_boi[(nums[idx] + 1):], idx=idx + 1)

        ans += solve_rec(og_boi=og_boi[1:], idx=idx) if og_boi[0] != '#' else 0

        return ans

    return solve_rec(idx=0, og_boi=og_boi)


def solve2(data):
    s = 0
    for x in tqdm(data):
        x = x.split()

        x[0] = (x[0] + "?") * 5
        x[1] = (x[1] + ',') * 5

        x[0] = x[0][:-1]
        x[1] = x[1][:-1]

        nums = [int(it) for it in x[1].split(",")]

        ans = generate2(nums=nums, og_boi=tuple(x[0]))

        # print(x)
        # print(ans)
        s += ans
    print(s)


def main():
    with open("data.txt") as f:
        data = f.read().splitlines()
        solve2(data)


if __name__ == "__main__":
    """
    ?###???????? 3,2,1
    """
    start = time.time()
    main()
    print(f"Time taken: {time.time() - start:1f}s")

    with open("data.txt") as f:
        lines = f.read().splitlines()

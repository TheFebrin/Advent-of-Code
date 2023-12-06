def solve(t, d):
    ans = 0
    for i in range(t):
        remaining = t - i
        dist = remaining * i
        if dist > d:
            ans += 1
    return ans


def main():
    data = [
        # (7, 9),
        # (15, 40),
        # (30, 200)

        # (47, 282),
        # (70, 1079),
        # (75, 1147),
        # (66, 1062)

        (47707566, 282107911471062)
    ]
    ans = 1
    for t, d in data:
        ans *= solve(t, d)

    print(ans)

if __name__ == "__main__":
    main()
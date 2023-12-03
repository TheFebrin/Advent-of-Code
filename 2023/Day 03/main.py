MAP = []
MAP2 = []

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

visited = set()

def BFS(x, y):
    it = y
    while y >= 0 and MAP[x][y].isdigit():
        visited.add((x, y))
        MAP2[x][y] = MAP[x][y]
        y -= 1

    y = it + 1
    while y < len(MAP[x]) and MAP[x][y].isdigit():
        visited.add((x, y))
        MAP2[x][y] = MAP[x][y]
        y += 1

def solve1():
    for i in range(len(MAP)):
        row = MAP[i]
        for j in range(len(row)):
            x = row[j]
            if not x.isdigit() and x != '.':
                for k in range(len(dx)):
                    new_x = i + dx[k]
                    new_y = j + dy[k]
                    if 0 <= new_x < len(MAP) and 0 <= new_y < len(MAP[0]):
                        if MAP[new_x][new_y].isdigit() and (new_x, new_y) not in visited:
                            BFS(new_x, new_y)

    ans = 0
    for row in MAP2:
        x = "".join(row).strip().split()
        for it in x:
            ans += int(it)
    print(ans)


def BFS2(x, y):
    num = []
    it = y
    while y >= 0 and MAP[x][y].isdigit():
        visited.add((x, y))
        MAP2[x][y] = MAP[x][y]
        num = [MAP[x][y]] + num
        y -= 1

    y = it + 1
    while y < len(MAP[x]) and MAP[x][y].isdigit():
        visited.add((x, y))
        MAP2[x][y] = MAP[x][y]
        num.append(MAP[x][y])
        y += 1
    return int("".join(num))

def solve2():
    ans = 0
    for i in range(len(MAP)):
        row = MAP[i]
        for j in range(len(row)):
            x = row[j]
            scores = []
            if not x.isdigit() and x != '.':
                for k in range(len(dx)):
                    new_x = i + dx[k]
                    new_y = j + dy[k]
                    if 0 <= new_x < len(MAP) and 0 <= new_y < len(MAP[0]):
                        if MAP[new_x][new_y].isdigit() and (new_x, new_y) not in visited:
                            bfs_res = BFS2(new_x, new_y)
                            scores.append(bfs_res)
            if len(scores) == 2:
                ans += scores[0] * scores[1]

    # ans = 0
    # for row in MAP2:
    #     x = "".join(row).strip().split()
    #     for it in x:
    #         ans += int(it)
    print(ans)

def main():
    with open("data.txt") as f:
        data = f.read().splitlines()
        for x in data:
            MAP.append(list(x))
            MAP2.append([" "] * len(x))
        solve2()

if __name__ == "__main__":
    main()
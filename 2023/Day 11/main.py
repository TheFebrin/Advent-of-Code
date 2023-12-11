from collections import deque

from tqdm import tqdm


def BFS(data, x, y, calculated):
    Q = deque()
    dist = [[-1 for _ in range(len(data[0]))] for _ in range(len(data))]
    dist[x][y] = 0
    Q.append((x, y))
    while Q:
        actual = Q.popleft()
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            nx = actual[0] + dx[i]
            ny = actual[1] + dy[i]
            if 0 <= nx < len(data) and 0 <= ny < len(data[0]) and dist[nx][ny] == -1:
                Q.append((nx, ny))
                dist[nx][ny] = dist[actual[0]][actual[1]] + 1

    ans = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) in calculated or (j, i) in calculated:
                continue
            if data[i][j] == "#":
                # print("dist ", x, y, " => ", i, j, " = ", dist[i][j])
                ans.append(dist[i][j])
    # print(len(ans))
    return sum(ans)


def solve(data):
    data2 = []
    for i, x in enumerate(data):
        data2.append(x)
        if x.count("#") == 0:
            data2.append(x)

    data3 = [[] for _ in range(len(data2))]
    for j in range(len(data2[0])):
        for i in range(len(data2)):
            data3[i].append(data2[i][j])
        if sum([data2[i][j] == "#" for i in range(len(data2))]) == 0:
            for i in range(len(data2)):
                data3[i].append(data2[i][j])

    for x in data3:
        print(*x)

    print(len(data), len(data[0]))
    print(len(data3), len(data3[0]))

    ans = 0
    calculated = set()
    # for i in tqdm(range(len(data3))):
    #     for j in range(len(data3[0])):
    #         if data3[i][j] == "#":
    #             ans += BFS(data3, i, j, calculated)
    #             calculated.add((i, j))
                # print(calculated)

    galaxies = []
    for i in tqdm(range(len(data3))):
        for j in range(len(data3[0])):
            if data3[i][j] == "#":
                galaxies.append((i, j))

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            ans += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
    print(ans)


def solve2(data):
    rows, cols = [], []
    for i, x in enumerate(data):
        if x.count("#") == 0:
            rows.append(i)

    for j in range(len(data[0])):
        if sum([data[i][j] == "#" for i in range(len(data))]) == 0:
            cols.append(j)


    ans = 0
    galaxies = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "#":
                galaxies.append((i, j))

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            act = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            for x in rows:
                if galaxies[i][0] <= x <= galaxies[j][0] or galaxies[j][0] <= x <= galaxies[i][0]:
                    act += 1_000_000 - 1

            for y in cols:
                if galaxies[i][1] <= y <= galaxies[j][1] or galaxies[j][1] <= y <= galaxies[i][1]:
                    act += 1_000_000 - 1
            # print(galaxies[i], galaxies[j], " => ", act)
            ans += act
    print(ans)
    # 597714715262 high
    # 597714117556

def main():
    with open("data.txt") as f:
        data = f.read().splitlines()
        solve2(data)


if __name__ == "__main__":
    main()

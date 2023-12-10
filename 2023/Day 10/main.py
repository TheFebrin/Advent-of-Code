from collections import deque

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

pipe_to_direction = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
}


def solve(data):
    map = []
    map_dist = []
    for i, x in enumerate(data):
        map.append(list(x))
        map_dist.append([-1] * len(x))
        for j, y in enumerate(list(x)):
            if y == "S":
                start = (i, j)

    # for x in map:
    #     print(x)

    Q = deque()
    Q.append(start)
    map_dist[start[0]][start[1]] = 0
    map[start[0]][start[1]] = "J"
    while len(Q) > 0:
        act = Q.popleft()

        for dx, dy in pipe_to_direction[map[act[0]][act[1]]]:
            new_x = act[0] + dx
            new_y = act[1] + dy
            if 0 <= new_x < len(map) and 0 <= new_y < len(map[0]) and map[new_x][new_y] != '.' and map_dist[new_x][
                new_y] == -1:
                map_dist[new_x][new_y] = map_dist[act[0]][act[1]] + 1
                Q.append((new_x, new_y))

    for x in map_dist:
        print(x)

    print(max([max(x) for x in map_dist]))


def solve2(data):
    map = []
    map_dist = []
    for i, x in enumerate(data):
        new_row = []
        for j, y in enumerate(list(x)):
            new_row.append(y)
            new_row.append(" ")
        map.append(new_row)
        map.append([" "] * len(new_row))
        map_dist.append([-1] * len(new_row))
        map_dist.append([-1] * len(new_row))

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "S":
                start = (i, j)

    for x in map:
        print("".join(x))

    Q = deque()
    Q.append(start)
    map_dist[start[0]][start[1]] = 0
    # map[start[0]][start[1]] = "J"
    map[start[0]][start[1]] = "F"
    while len(Q) > 0:
        act = Q.popleft()
        for dx, dy in pipe_to_direction[map[act[0]][act[1]]]:
            new_x = act[0] + dx * 2
            new_y = act[1] + dy * 2
            new_x_middle = act[0] + dx
            new_y_middle = act[1] + dy

            if 0 <= new_x < len(map) and 0 <= new_y < len(map[0]) and map[new_x][new_y] != '.' and (
                    map_dist[new_x][new_y] == -1 or map_dist[new_x_middle][new_y_middle] == -1):
                map_dist[new_x][new_y] = map_dist[act[0]][act[1]] + 1
                map_dist[new_x_middle][new_y_middle] = map_dist[act[0]][act[1]] + 1
                Q.append((new_x, new_y))


    for x in map_dist:
        for y in x:
            if y == -1:
                print(".", end="")
            else:
                print("x", end="")
        print()

    for i in range(len(map)):
        if map_dist[i][0] == -1:
            Q.append((i, 0))

        if map_dist[i][len(map[0]) - 1] == -1:
            Q.append((i, len(map[0]) - 1))
    for j in range(len(map[0])):
        if map_dist[0][j] == -1:
            Q.append((0, j))

        if map_dist[len(map) - 1][j] == -1:
            Q.append((len(map) - 1, j))

    while len(Q) > 0:
        act = Q.popleft()
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        map_dist[act[0]][act[1]] = 0
        for k in range(4):
            new_x = act[0] + dx[k]
            new_y = act[1] + dy[k]
            if 0 <= new_x < len(map) and 0 <= new_y < len(map[0]) and map_dist[new_x][new_y] == -1:
                map_dist[new_x][new_y] = 0
                Q.append((new_x, new_y))

    for x in map_dist:
        print(x)

    ans = 0
    for i, x in enumerate(map_dist):
        for j, y in enumerate(x):
            if i % 2 == 1 or j % 2 == 1:
                print("f", end="")
                continue
            if map_dist[i][j] == -1:
                ans += 1
                print("!", end="")
            else:
                print(".", end="")
        print()

    print(ans)


def main():
    with open("data.txt") as f:
        data = f.read().splitlines()
        solve2(data)


if __name__ == "__main__":
    main()

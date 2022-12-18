
from typing import *
import heapq
from tqdm import tqdm


def BFS_marker(grid: List[List[str]], dist: int, start: Tuple[int, int]):
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, start)
    
    visited = set()

    while len(heap) > 0:
        act_state = heapq.heappop(heap)
        visited.add(act_state)

        if grid[act_state[0]][act_state[1]] not in ("S", "B"):
            grid[act_state[0]][act_state[1]] = '#'

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            new_point = (act_state[0] + dx[i], act_state[1] + dy[i])
            if 0 <= new_point[0] and 0 <= new_point[1] and new_point not in visited:
                act_dist = abs(start[0] - new_point[0]) + abs(start[1] - new_point[1])
                if act_dist <= dist:
                    heapq.heappush(heap, new_point)
                    visited.add(new_point)


def solve1() -> None:
    MAP = [
        ["." for j in range(1000)]
        for i in range(1000)
    ]
    cords = []
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.strip()
            line = line.replace(
                "Sensor at ",
                ""
            ).replace(
                "closest beacon is at ",
                ""
            ).replace(
                "x=",
                ""
            ).replace(
                "y=",
                ""
            ).replace(
                ":",
                ","
            )
            sensor_x, sensor_y, beacon_x, beacon_y = map(int, line.split(","))
            cords.append((sensor_x, sensor_y, beacon_x, beacon_y))

    most_negative = -10
    for t in cords:
        sensor_x, sensor_y, beacon_x, beacon_y = t
        sensor_x += abs(most_negative)
        sensor_y += abs(most_negative)
        beacon_x += abs(most_negative)
        beacon_y += abs(most_negative)
        MAP[sensor_y][sensor_x] = "S"
        MAP[beacon_y][beacon_x] = "B"
        dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        BFS_marker(
            grid=MAP,
            dist=dist,
            start=(sensor_y, sensor_x)
        )

    # for i, row in enumerate(MAP[:23]):
    #     print(i, row[:20])

    # print(*MAP[8 - most_negative][:25])
    # print(*MAP[9 - most_negative][:25])
    # print(*MAP[10 - most_negative][:25])
    # print(*MAP[11 - most_negative][:25])
    # print(*MAP[12 - most_negative][:25])
    print(MAP[10 - most_negative].count("#"))


def solve1_round2() -> None:
    beacons, sensors = [], []
    far_l, far_r = 0, 0
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.strip()
            line = line.replace(
                "Sensor at ",
                ""
            ).replace(
                "closest beacon is at ",
                ""
            ).replace(
                "x=",
                ""
            ).replace(
                "y=",
                ""
            ).replace(
                ":",
                ","
            )
            sensor_x, sensor_y, beacon_x, beacon_y = map(int, line.split(","))
            dist: int = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            sensors.append((
                sensor_y, sensor_x, dist
            ))
            beacons.append((beacon_y, beacon_x))
            far_l = min(far_l, beacon_x - dist)
            far_r = max(far_r, beacon_x + dist)

    ans = 0
    Y = 2000000
    print(f"From: {far_l} to {far_r}")
    for j in tqdm(range(far_l, far_r + 1)):
        good = False
        for x, y, d in sensors:
            dist = abs(x - Y) + abs(j - y)
            if dist > 0 and dist <= d and not (Y, j) in beacons:
                good = True
                # print(j, " => ", x, y, f" ||| {dist} <= {d}")
                break
        if good:
            ans += 1
    
    print("ans: ", ans)


def find_empty_guy(arr: List[Tuple[int, int]]) -> Optional[int]:
    assert arr[0][0] <= 0, "sanity check"
    biggest = arr[0][1]
    for x, y in arr:
        if x > biggest + 1:
            print(f"Found empty guy! biggest: {biggest}: <{x, y}> : {arr}")
            print("Column: ", biggest + 1)
            return biggest + 1
        biggest = max(biggest, y)
    return None


def solve2() -> None:
    beacons, sensors = [], []
    distances = [[] for _ in range(4000042)]

    far_l, far_r = 0, 0
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.strip()
            line = line.replace(
                "Sensor at ",
                ""
            ).replace(
                "closest beacon is at ",
                ""
            ).replace(
                "x=",
                ""
            ).replace(
                "y=",
                ""
            ).replace(
                ":",
                ","
            )
            sensor_x, sensor_y, beacon_x, beacon_y = map(int, line.split(","))
            dist: int = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            sensors.append((
                sensor_y, sensor_x, dist
            ))
            beacons.append((beacon_y, beacon_x))
            # print(f"Sensor {sensor_y} {sensor_x} dist: {dist}")
            idx = 0
            for i in range(sensor_y - dist, sensor_y + dist + 1):
                if i < 0 or i >= 4000042:
                    idx += 1
                    continue

                if i <= sensor_y:
                    distances[i].append((sensor_x - idx, sensor_x + idx))
                else:
                    distances[i].append((
                        sensor_x - (2 * dist - idx), sensor_x + (2 * dist - idx)
                    ))
                idx += 1

    for x in tqdm(distances):
        x.sort()

    for i, x in tqdm(enumerate(distances)):
        # print(i, x)
        column = find_empty_guy(arr=x)
        if column is not None:
            print(f"Row: {i} column: {column}")
            print(f"Ans: {column * 4000000 + i}")
            return


def main() -> None:
    solve2()

if __name__ == '__main__':
    main()


from typing import *
import heapq
from tqdm import tqdm
from dataclasses import dataclass


@dataclass(frozen=True)
class State:
    x: int
    y: int
    steps: int
    history: List[Tuple[int, int]]


    def __eq__(self, __o: object) -> bool:
        return self.steps == __o.steps

    def __lt__(self, __o: object) -> bool:
        return self.steps < __o.steps


def BFS(grid: List[List[str]], start: Tuple[int, int]) -> State:
    visited = [
        [False for j in range(len(grid[0]))]
        for i in range(len(grid))
    ]
    visited[start[0]][start[1]] = True

    grid[start[0]][start[1]] = "a"
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, State(x=start[0], y=start[1], steps=0, history=[]))

    while len(heap) > 0:
        act_state = heapq.heappop(heap)

        if grid[act_state.x][act_state.y] == "E":
            # print('Done -> ', act_state.steps)
            return act_state

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        curr_height = ord(grid[act_state.x][act_state.y])
        for i in range(4):
            new_point = (act_state.x + dx[i], act_state.y + dy[i])
            if 0 <= new_point[0] < len(grid) and 0 <= new_point[1] < len(grid[0]):
                if not visited[new_point[0]][new_point[1]]:
                    if (ord(grid[new_point[0]][new_point[1]]) - curr_height <= 1 and grid[new_point[0]][new_point[1]] != "E") \
                        or (grid[new_point[0]][new_point[1]] == "E" and ord('z') - curr_height <= 1):
                        heapq.heappush(
                            heap, 
                            State(
                                x=new_point[0], 
                                y=new_point[1], 
                                steps=act_state.steps + 1, 
                                history=act_state.history + [(act_state.x, act_state.y)]
                            )
                        )
                        visited[new_point[0]][new_point[1]] = True


def main() -> None:
    grid = []
    with open("data.txt") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))

    start = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start = (i, j)
                break
    assert start is not None

    end_state = BFS(grid=grid, start=start)
    print("ans: ", end_state.steps)
    print('\n\n Part 2 \n\n')
    
    ans = []
    for i in tqdm(range(len(grid))):
        for j in range(len(grid[0])):
            if grid[i][j] == "a":
                end_state = BFS(grid=grid, start=(i, j))
                if end_state is not None:
                    ans.append(end_state.steps)

    print(sorted(ans))


if __name__ == __name__:
    main()
from typing import *


def is_visible(grid: List[List[int]], x: int, y: int) -> bool:
    h = grid[x][y]
    blocked = 0
    for i in range(x + 1, len(grid)):
        if grid[i][y] >= h:
            blocked += 1
            break
        
    for i in range(0, x):
        if grid[i][y] >= h:
            blocked += 1
            break
        
    for j in range(y + 1, len(grid[0])):
        if grid[x][j] >= h:
            blocked += 1
            break
        
    for j in range(0, y):
        if grid[x][j] >= h:
            blocked += 1
            break
            
    return blocked != 4
    
    
def solve1() -> None:
    grid = []
    with open("data.txt") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # if i == 0 or i == len(grid) - 1:
            #     continue
            # if j == 0 or j == len(grid[0]) - 1:
            #     continue
            if is_visible(grid, i, j):
                ans += 1
                # print(i, j, grid[i][j])
    
    print(ans)
    
 
def calculate_score(grid: List[List[int]], x: int, y: int) -> int:
    h = grid[x][y]
    score = 1
    ile = 0
    for i in range(x + 1, len(grid)):
        ile += 1
        if grid[i][y] >= h:
            break
        
    score *= ile
    # print("going down: ", ile)
        
    ile = 0
    for i in reversed(range(0, x)):
        ile += 1
        if grid[i][y] >= h:
            break
    score *= ile
    # print("going up: ", ile)
     
    ile = 0
    for j in range(y + 1, len(grid[0])):
        ile += 1
        if grid[x][j] >= h:
            break
    score *= ile
    # print("going right: ", ile)
     
     
    ile = 0
    for j in reversed(range(0, y)):
        ile += 1
        if grid[x][j] >= h:
            break
    score *= ile
    # print("going left: ", ile)
     
    return score
        
def solve2() -> None:
    grid = []
    with open("data.txt") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            score = calculate_score(grid, i, j)
            ans = max(ans, score)
    
    print(ans)
    
def main() -> None:
    solve2()

if __name__ == __name__:
    main()
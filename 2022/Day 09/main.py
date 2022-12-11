from typing import *


def adapt_tail_position(
    tail_position: Tuple[int, int],
    head_position: Tuple[int, int]
) -> Tuple[int, int]:
    # diagonal case 2nd task
    if abs(head_position[0] - tail_position[0]) == 2 \
        and abs(head_position[1] - tail_position[1]) == 2:
            vx = head_position[0] - tail_position[0]
            vy = head_position[1] - tail_position[1]
            return (
                tail_position[0] + vx // 2,
                tail_position[1] + vy // 2
            )
        
    if tail_position[0] == head_position[0]:
        if abs(head_position[1] - tail_position[1]) != 2:
            return tail_position
        
        if tail_position[1] > head_position[1]:
            return (
                tail_position[0],
                tail_position[1] - 1
            )
        else:
            return (
                tail_position[0],
                tail_position[1] + 1
            )
    
    if tail_position[1] == head_position[1]:
        if abs(head_position[0] - tail_position[0]) != 2:
            return tail_position
        if tail_position[0] > head_position[0]:
            return (
                tail_position[0] - 1,
                tail_position[1]
            )
        else:
            return (
                tail_position[0] + 1,
                tail_position[1]
            )
        
    # Diagonal case
    if abs(head_position[0] - tail_position[0]) == 2:
        return adapt_tail_position(
            tail_position=(
                tail_position[0],
                head_position[1]
            ),
            head_position=head_position
        )
    elif abs(head_position[1] - tail_position[1]) == 2:
        return adapt_tail_position(
            tail_position=(
                head_position[0],
                tail_position[1]
            ),
            head_position=head_position
        )
    else:
        return tail_position
    
    
def solve1() -> None:
    head_position = [0, 0]
    tail_position = [0, 0]
    ans = set()
    with open("data.txt") as f:
        for line in f.readlines():
            direction, steps = line.split()
            for _ in range(int(steps)):
                if direction == "U":
                    head_position[0] -= 1
                elif direction == "D":
                    head_position[0] += 1
                elif direction == "R":
                    head_position[1] += 1
                elif direction == "L":
                    head_position[1] -= 1
                
                tail_position = adapt_tail_position(
                    tail_position=tail_position,
                    head_position=head_position,
                )
                print(head_position, " -> ", tail_position)
                ans.add(tuple(tail_position))
    print(len(ans))   
        
      
def visualize(tail: List[Tuple[int, int]]) -> None:
    N = 10
    grid = [
        ["." for i in range(N)]
        for j in range(N)
    ]  
    for i in range(len(tail)):
        x, y = tail[i]
        x = N + x - 1
        
        if i == 0:
            grid[x][y] = "H"
        else:
            grid[x][y] = str(i)
        
    for row in grid:
        print(*row)
    
    print('\n\n ======== \n\n ')
def solve2() -> None:
    tail_position = [[0, 0] for _ in range(10)]
    ans = set()
    with open("data.txt") as f:
        for line in f.readlines():
            direction, steps = line.split()
            for _ in range(int(steps)):
                if direction == "U":
                    tail_position[0][0] -= 1
                elif direction == "D":
                    tail_position[0][0] += 1
                elif direction == "R":
                    tail_position[0][1] += 1
                elif direction == "L":
                    tail_position[0][1] -= 1
                
                for i in range(9):
                    tail_position[i + 1] = adapt_tail_position(
                        tail_position=tail_position[i + 1],
                        head_position=tail_position[i],
                    )
                # print(head_position, " -> ", tail_position)
                ans.add(tuple(tail_position[-1]))
                # visualize(tail_position)
    print(len(ans))   
    
    
def main() -> None:
    solve2()

if __name__ == __name__:
    main()
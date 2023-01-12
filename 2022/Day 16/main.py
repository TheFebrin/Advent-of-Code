import time
from typing import *

def solve() -> None:
    G = {}
    rates = {}
    distances = {}
    nodes = set()
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.split()
            valve = line[1]
            rate = int(line[4].split("=")[1].strip(';'))
            neighbours = list(map(lambda x: x.strip(','), line[9:]))
            
            nodes.add(valve)
            G[valve] = neighbours
            if rate > 0:
                rates[valve] = rate
            
    for v in nodes:
        distances[v] = {}
        for w in nodes:
            distances[v][w] = 1_000_000_000
    
    for v in nodes:
        distances[v][v] = 0
        for w in G[v]:
            distances[v][w] = 1
            distances[w][v] = 1
        
    for k in nodes:
        for i in nodes:  
            for j in nodes:
                distances[i][j] = min(
                    distances[i][j], 
                    distances[i][k] + distances[k][j]
                )
    
    states_visited: int = 0
    memo: Dict[Tuple[int, str, set], int] = {}
    
    def solve1(
        t: int, 
        act_node: str, 
        not_opened: set,
    ) -> int:
        nonlocal states_visited
        states_visited += 1
        
        if (t, act_node, tuple(sorted(not_opened))) in memo:
            return memo[t, act_node, tuple(sorted(not_opened))]
                        
        ans = [0]
        for c in not_opened:
            # open node
            remaining_time: int = t - 1 - distances[act_node][c]
            if remaining_time > 0:
                gain = rates[c] * remaining_time
                backtrack_gain = solve1(
                    t=remaining_time,
                    act_node=c,
                    not_opened=not_opened - {c},
                )
                ans.append(gain + backtrack_gain)
                
        memo[t, act_node, tuple(sorted(not_opened))] = max(ans)
        return max(ans)
            
    print(rates.keys())
    answer = solve1(
        t=30,
        act_node="AA",
        not_opened=rates.keys(),
    )
    print("Task 1: ", answer)
    print(f"States visited: ", states_visited)
    
    
    states_visited = 0
    def solve2(
        t: int, 
        elefant_t: int,
        act_node: str, 
        elefant_node: str,
        not_opened: set,
    ) -> int:
        nonlocal states_visited
        states_visited += 1
        
        if (
            t, elefant_t, act_node, elefant_node,
            tuple(sorted(not_opened)), 
        ) in memo:
            return memo[
                t, elefant_t, act_node, elefant_node,
                tuple(sorted(not_opened)), 
            ]
                        
        ans = [0]
        for c in not_opened:
            for c2 in not_opened:
                if c == c2:
                    continue
                # open node
                remaining_time: int = t - 1 - distances[act_node][c]
                remaining_time_e: int = elefant_t - 1 - distances[elefant_node][c2]
                if remaining_time > 0 and remaining_time_e > 0:
                    gain = rates[c] * remaining_time + rates[c2] * remaining_time_e
                    backtrack_gain = solve2(
                        t=remaining_time,
                        elefant_t=remaining_time_e,
                        act_node=c,
                        elefant_node=c2,
                        not_opened=not_opened - {c, c2},
                    )
                    ans.append(gain + backtrack_gain)
                
        memo[
            t, elefant_t, act_node, elefant_node,
            tuple(sorted(not_opened)),
        ] = max(ans)
        return max(ans)
    
    answer2 = solve2(
        t=26,
        elefant_t=26,
        act_node="AA",
        elefant_node="AA",
        not_opened=rates.keys(),
    )
    print('Task 2: ', answer2)
    

def main() -> None:
    start = time.time()
    solve()
    print(f"Took: {time.time() - start:.2f}s")

if __name__ == '__main__':
    main()


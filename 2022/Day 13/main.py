from typing import *
import json
from copy import deepcopy

def check(l1: List[Any], l2: List[Any], steps: int) -> Optional[bool]:
    # print("\t" * steps + f"- Compare {l1} vs {l2}")
    
    if len(l1) == 0 and len(l2) == 0:
        # print("both empty")
        return None
    elif len(l1) > 0 and len(l2) > 0:
        # print("both not empty")
        pass
    elif len(l1) > 0 and len(l2) == 0:
        # print("l2 empty")
        return False
    elif len(l1) == 0 and len(l2) > 0:
        # print("l1 empty")
        return True
    
    l1_front = l1.pop(0)
    l2_front = l2.pop(0)
    
    print("\t" * steps + f"- Compare {l1_front} vs {l2_front}")

    if type(l1_front) is int and type(l2_front) is int:
        # print('both int')
        if l1_front == l2_front:
            return check(l1=l1, l2=l2, steps=steps + 1)
        return l1_front < l2_front
    elif type(l1_front) is list and type(l2_front) is list:
        if (ch1 := check(l1=l1_front, l2=l2_front, steps=steps)) is not None:
            return ch1
        return check(l1=l1, l2=l2, steps=steps + 1)
    elif type(l1_front) is int and type(l2_front) is list:
        if (ch1 := check(l1=[l1_front], l2=l2_front, steps=steps)) is not None:
            return ch1
        return check(l1=l1, l2=l2, steps=steps + 1)
    elif type(l1_front) is list and type(l2_front) is int:
        if (ch1 := check(l1=l1_front, l2=[l2_front], steps=steps)) is not None:
            return ch1
        return check(l1=l1, l2=l2, steps=steps + 1)


def main() -> None:
    arrays = []
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                pass
            else:
                arrays.append(json.loads(line))
                
    res = []
    for i in range(0, len(arrays), 2):
        print(f"== Pair {i  // 2 + 1} ==")
        print(f"- Compare {arrays[i]} vs {arrays[i + 1]}")
        ans = check(l1=arrays[i], l2=arrays[i + 1], steps=0)
        if ans:
            res.append(i // 2 + 1)

        print(f"{i // 2  + 1} are in right order? {ans}")
        print('\n\n ======== \n\n')
    print(res)
    print(sum(res))


if __name__ == __name__:
    main()
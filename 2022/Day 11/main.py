from __future__ import annotations

import math
from uuid import uuid4
from typing import *
from tqdm import tqdm
from functools import reduce
from dataclasses import dataclass, field


@dataclass(frozen=False)
class Item:
    uid: int
    value: int


@dataclass(frozen=False)
class Monke:
    id: int
    items: List[Item]
    operation: Callable[[int], int]
    test: Callable[[int], bool]
    action_if_test_true: int
    action_if_test_false: int
    items_inspected: int = field(init=False)

    def __post_init__(self) -> None:
        self.items_inspected = 0

    @staticmethod
    def get_operation(raw_operation: str) -> Callable[[int], int]:
        raw_operation = raw_operation.split()
        op = raw_operation[4]
        val = raw_operation[5]
    
        if op == "+":
            if val == "old":
                return lambda x: x + x
            else:
                return lambda x: x + int(val)
        elif op == "*":
            if val == "old":
                return lambda x: x * x
            else:
                return lambda x: x * int(val)
        else:
            raise RuntimeError(raw_operation)

    @staticmethod
    def get_test(raw_test: str) -> Callable[[int], bool]:
        raw_test = raw_test.split()
        return lambda x: x % int(raw_test[-1]) == 0

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def play_round(self, monkes: List[Monke], divide: bool = True, lcm: Optional[int] = None) -> None:
        while len(self.items) > 0:
            item = self.items.pop(0)
            self.items_inspected += 1

            item.value = self.operation(item.value)
            if lcm is not None:
                item.value = item.value % lcm

            if divide:
                item.value = item.value // 3

            if self.test(item.value):
                monkes[self.action_if_test_true].add_item(item=item)
            else:
                monkes[self.action_if_test_false].add_item(item=item)


def solve1() -> None:
    data = []
    with open("data.txt") as f:
        for line in f.readlines():
            data.append(line.strip())
    
    monkes: List[Monke] = []
    for i in range(0, len(data), 7):
        monke_raw = data[i:i + 7]
        monke = Monke(
            id=int(monke_raw[0].split()[1][:-1]),
            items=list(map(lambda x: Item(uid=uuid4().hex, value=int(x)), monke_raw[1][15:].split(','))),
            operation=Monke.get_operation(raw_operation=monke_raw[2]),
            test=Monke.get_test(raw_test=monke_raw[3]),
            action_if_test_true=int(monke_raw[4].split()[-1]),
            action_if_test_false=int(monke_raw[5].split()[-1]),
        )
        monkes.append(monke)

    for i in tqdm(range(20)):
        for monke in monkes:
            monke.play_round(monkes=monkes, divide=True)

    ans = []
    for monke in monkes:
        print(monke.items_inspected)
        ans.append(monke.items_inspected)

    
    print('Ans:')
    print(reduce(lambda x, y: x * y, sorted(ans, reverse=True)[:2]))


def solve2() -> None:
    data = []
    with open("data.txt") as f:
        for line in f.readlines():
            data.append(line.strip())
    
    monkes: List[Monke] = []
    for i in range(0, len(data), 7):
        monke_raw = data[i:i + 7]
        monke = Monke(
            id=int(monke_raw[0].split()[1][:-1]),
            items=list(map(lambda x: Item(uid=uuid4().hex, value=int(x)), monke_raw[1][15:].split(','))),
            operation=Monke.get_operation(raw_operation=monke_raw[2]),
            test=Monke.get_test(raw_test=monke_raw[3]),
            action_if_test_true=int(monke_raw[4].split()[-1]),
            action_if_test_false=int(monke_raw[5].split()[-1]),
        )
        monkes.append(monke)

    divisors = [int(data[i:i + 7][3].split()[-1]) for i in range(0, len(data), 7)]
    gcd = reduce(lambda x, y: math.gcd(x, y), divisors)
    print(divisors)
    lcm = reduce(lambda x, y: x * y, divisors) // gcd
    print('lcm: ', lcm)
    
    for i in tqdm(range(10000)):
        for monke in monkes:
            monke.play_round(monkes=monkes, divide=False, lcm=lcm)

    ans = []
    for monke in monkes:
        print(monke.items_inspected)
        ans.append(monke.items_inspected)

    print('Ans:')
    print(reduce(lambda x, y: x * y, sorted(ans, reverse=True)[:2]))


def main() -> None:
    solve2()


if __name__ == __name__:
    main()
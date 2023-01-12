
from typing import *


class Line:
    """
    ####
    """
    
    def __init__(self, row: int) -> None:
        self.row = row
        self.column = 2
    
    def move_left(self) -> None:
        if self.column > 0:
            self.column -= 1
    
    def move_right(self) -> None:
        if self.column < 3:
            self.column += 1
            
    def move_down(self) -> None:
        self.row -= 1
    
    def can_fall_down(self, map) -> bool:
        pass
            
class Plus:
    """
    .#.....
    ###....
    .#.....
    
    .....#.
    ....###
    .....#.
    """
    
    def __init__(self, row: int) -> None:
        self.row = row
        self.column = 2
    
    def move_left(self) -> None:
        if self.column > 0:
            self.column -= 1
    
    def move_right(self) -> None:
        if self.column < 4:
            self.column += 1
    
    def move_down(self) -> None:
        self.row -= 1
    
    def can_fall_down(self, map) -> bool:
        pass
            
class L:
    """
    ####
    """
    
    def __init__(self, row: int) -> None:
        self.row = row
        self.column = 2
    
    def move_left(self) -> None:
        if self.column > 0:
            self.column -= 1
    
    def move_right(self) -> None:
        if self.column < 4:
            self.column += 1
            
    def move_down(self) -> None:
        self.row -= 1
    
    def can_fall_down(self, map) -> bool:
        pass
    
    
class I:
    """
    ####
    """
    
    def __init__(self, row: int) -> None:
        self.row = row
        self.column = 2
    
    def move_left(self) -> None:
        if self.column > 0:
            self.column -= 1
    
    def move_right(self) -> None:
        if self.column < 6:
            self.column += 1
    
    def move_down(self) -> None:
        self.row -= 1
    
    def can_fall_down(self, map) -> bool:
        pass
    
         
class Square:
    """
    ####
    """
    
    def __init__(self, row: int) -> None:
        self.row = row
        self.column = 2
    
    def move_left(self) -> None:
        if self.column > 0:
            self.column -= 1
    
    def move_right(self) -> None:
        if self.column < 5:
            self.column += 1
            
    def move_down(self) -> None:
        self.row -= 1
    
    def can_fall_down(self, map) -> bool:
        pass
     
        
class Engine:
    
    def __init__(self, pattern: str) -> None:
        self.map = []
        self.pattern = pattern
        self.shapes = [
            Line, Plus, L, I, Square
        ]
        self.actual_shape = None
        self.time = 0

    def add_shape(self) -> None:
        ...
        
    def run(self, limit: int):
        while self.time < limit:
            # gas push
            char = self.pattern[self.time]
            if char == '<':
                self.actual_shape.move_left()
            elif char == ">":
                self.actual_shape.move_right()
            else:
                raise RuntimeError
            # fall down
            
            if self.actual_shape.row > 0 and self.actual_shape.can_fall_down(map=self.map):
                self.actual_shape.move_down()
            else:
                # freeze shape
                self.add_shape()
                
                # render new shape
                
            
            
            self.time += 1
        
        
        
def solve1() -> None:
    pattern = open("data.txt").readline().strip()


    n_rocks = 2022
    
    
def solve2() -> None:
    ...

def main() -> None:
    solve1()

if __name__ == '__main__':
    main()


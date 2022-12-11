from __future__ import annotations
from typing import *
from dataclasses import dataclass


@dataclass
class File:
    name: str
    size: int


class Dir:
    
    def __init__(
        self, 
        parent: Dir, 
        name: str, 
        children: List[Dir],
        files: List[File]
    ) -> None:
        self.parent =parent
        self.name = name
        self.children = children
        self.files = files
        
        
    def add_children(self, name: str) -> None:
        for c in self.children:
            if c.name == name:
                return
        
        # print(f'Added children: {name} to {self.name}')
        self.children.append(
            Dir(
                parent=self,
                name=name,
                children=[],
                files=[]
            )
        )
        
    def add_file(self, size: int, name: str) -> None:
        self.files.append(
            File(
                name=name,
                size=size
            )
        )
        
    def go_to_child(self, name: str) -> Dir:
        if name == "/":
            return self
        
        for c in self.children:
            if c.name == name:
                return c
        raise RuntimeError('Child not found')
    
    def get_dir_size(self) -> int:
        return sum(f.size for f in self.files) \
            + sum([c.get_dir_size() for c in self.children])
            
    def get_only_curr_dir_size(self) -> int:
        return sum(f.size for f in self.files)
    
    
def DFS(dir: Dir) -> int:
    ans = 0
    if dir.get_dir_size() <= 100000:
        print(dir.name, dir.get_dir_size())
        print(dir.files)
        ans = dir.get_dir_size()
        
    for c in dir.children:
       ans += DFS(c)
    
    return ans
    
    
def solve1() -> None:
    curr = Dir(
        parent = None,
        name = "/",
        children=[],
        files=[]
    )
    root = curr
    
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.split()
            # print(line)

            if line[0] == "$":
                if line[1] == "cd":
                    dest = line[2]
                    if dest == "..":
                        # print(f'Changing curr {curr.name} -> {curr.parent.name}')
                        curr = curr.parent
                    else:
                        curr = curr.go_to_child(
                            name=dest
                        )
                elif line[1] == "ls":
                    pass
            else:
                if line[0] == "dir":
                    curr.add_children(
                        name=line[1]
                    )
                else:
                    size = int(line[0])
                    file = line[1]
                    curr.add_file(
                        name=file,
                        size=size
                    )
    print(DFS(root))


def calculate_size_taken(dir: Dir) -> int:
    ans = dir.get_only_curr_dir_size()
    for c in dir.children:
       ans += calculate_size_taken(dir=c)
    return ans


can_delete = []
def find_dir_to_delete(dir: Dir, needed: int) -> int:
    # print('siema: ', dir.name, [c.name for c in dir.children])
    my_size = dir.get_only_curr_dir_size()
    for c in dir.children:
        # print(f'children size: {dir.name} -> {c.name}')
        my_size += find_dir_to_delete(c, needed=needed)

    if my_size >= needed:
        # print(f'Can delete dir: {dir.name}, {my_size}')
        can_delete.append(my_size)
    return my_size
        

def solve2() -> None:
    curr = Dir(
        parent = None,
        name = "/",
        children=[],
        files=[]
    )
    root = curr
    
    with open("data.txt") as f:
        for line in f.readlines():
            line = line.split()
            # print(line)

            if line[0] == "$":
                if line[1] == "cd":
                    dest = line[2]
                    if dest == "..":
                        # print(f'Changing curr {curr.name} -> {curr.parent.name}')
                        curr = curr.parent
                    else:
                        curr = curr.go_to_child(
                            name=dest
                        )
                elif line[1] == "ls":
                    pass
            else:
                if line[0] == "dir":
                    curr.add_children(
                        name=line[1]
                    )
                else:
                    size = int(line[0])
                    file = line[1]
                    curr.add_file(
                        name=file,
                        size=size
                    )
                    
    size_taken = calculate_size_taken(root)
    print("size_taken: ", size_taken)
    size_left = 70000000 - size_taken
    print("size_left: ", size_left)
    size_needed = 30000000 - size_left
    print("size_needed: ", size_needed)
    find_dir_to_delete(dir=root, needed=size_needed)
    print(sorted(can_delete))
    
    ans = sorted(can_delete)[0]
    assert size_left + ans >= 30000000
    print(f'ans: {ans}')
    
    """
    bad:
    7366500
    """
    
def main() -> None:
    solve2()

if __name__ == __name__:
    main()
import sys

map_ = [line.strip() for line in sys.stdin.readlines()]

def tree_finder(dx,dy):
    trees = 0
    x = 0
    y = 0
    while y<len(map_):
        if map_[y][x] == '#':
            trees += 1
        x = (x+dx)%len(map_[0])
        y += dy
    return trees

print(tree_finder(3,1))

print(
    tree_finder(1,1) *
    tree_finder(3,1) *
    tree_finder(5,1) *
    tree_finder(7,1) *
    tree_finder(1,2)
)

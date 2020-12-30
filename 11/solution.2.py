import sys
from collections import defaultdict
from copy import deepcopy

input_ = [list(line.strip()) for line in sys.stdin.readlines()]
nrows = len(input_)
ncols = len(input_[0])
area = defaultdict(lambda:{})
for r in range(nrows):
    for c in range(ncols):
        area[c+r*1j] = input_[r][c]

dirs = [(-1+0j),(-1-1j),(+0-1j),(+1-1j),(+1+0j),(+1+1j),(+0+1j),(-1+1j)]

def print_area(area):
    for r in range(nrows):
        for c in range(ncols):
            print(area[c+r*1j],end='')
        print()
    print()
    

def iterate_area(area):
    stable = True
    new_area = deepcopy(area)
    count =  deepcopy(area)
    for r in range(nrows):
        for c in range(ncols):
            pos = c+r*1j
            if area[pos]=='.':
                continue
            
            occupied = 0
            for d in dirs:
                pos = c+r*1j + d
                while pos in area:
                    if area[pos] == '#':
                        occupied += 1
                    if area[pos] != '.':
                        break
                    pos += d
            
            pos = c+r*1j
            count[pos] = occupied
            if occupied<=0:
                new_area[pos] = '#'
            elif occupied>=5:
                new_area[pos] = 'L'
            if area[pos]!=new_area[pos]:
                stable = False            
    #print_area(count)
    return stable,new_area


print_area(area)
stable = False
while not stable:
    stable,area = iterate_area(area)
    print_area(area)
print(list(area.values()).count('#'))

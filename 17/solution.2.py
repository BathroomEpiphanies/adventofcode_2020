import sys
import re
from collections import defaultdict
from functools import reduce
import networkx
from itertools import product,permutations,combinations
from copy import deepcopy

from lib.matrix import matrix

    
#neighbors = set(map(tuple,permutations([0,0,1],3))) | set(map(tuple,permutations([0,0,-1],3)))
neighbors = set(product([-1,0,1],[-1,0,1],[-1,0,1],[-1,0,1]))
neighbors.remove((0,0,0,0))
print(len(neighbors))
for n in neighbors:
    print(n)

#exit()
def print_cells(cells):
    minx = min(i for i,j,k in cells)
    maxx = max(i for i,j,k in cells)
    miny = min(j for i,j,k in cells)
    maxy = max(j for i,j,k in cells)
    minz = min(k for i,j,k in cells)
    maxz = max(k for i,j,k in cells)
    for z in range(minz,maxz+1):
        for y in range(miny,maxy+1):
            print(''.join([cells[(x,y,z)] if (x,y,z) in cells else '.' for x in range(minx,maxx+1)]))
        print()


def add(a,b):
    return tuple(c1+c2 for c1,c2 in zip(a,b))
def iterate(cells):
    new_cells = defaultdict(lambda:'.')
    def inner(coord):
        sum_ = 0
        for neigh in neighbors:
            if cells[add(coord,neigh)] == '#':
                sum_ += 1
        if cells[coord] == '#' and sum_ in [2,3] or sum_ == 3:
            new_cells[coord] = '#'
        else:
            new_cells[coord] = '.'
        
    for coord in list(cells):
        inner(coord)
        for neigh in neighbors:
            if add(coord,neigh) not in new_cells:
                inner(add(coord,neigh))
                
    return new_cells


cells = defaultdict(lambda:'.')
cells.update({(x,y,0,0):val for y,line in enumerate(sys.stdin.readlines()) for x,val in enumerate(line.strip())})
#print_cells(cells)


print()
print()
for i in range(6):
    print(i)
    cells = iterate(cells)
    #print_cells(cells)
    print()
    print()

count = list(cells.values()).count('#')
print(count)

import sys
from copy import deepcopy

area = [list(line.strip()) for line in sys.stdin.readlines()]

def print_area(area):
    for line in area:
        print(''.join(map(str,line)))
    print()

def iterate_area(area):
    stable = True
    new_area = deepcopy(area)
    count =  deepcopy(area)
    for r in range(len(area)):
        for c in range(len(area[r])):
            if area[r][c]=='.':
                continue
            elif area[r][c]=='#':
                occupied = -1
            else:
                occupied = 0
            for i in range(max(0,r-1),min(r+2,len(area))):
                for j in range(max(0,c-1),min(c+2,len(area[r]))):
                    if area[i][j] == '#':
                        occupied += 1
            count[r][c] = occupied
            if occupied<=0:
                new_area[r][c] = '#'
            elif occupied>=4:
                new_area[r][c] = 'L'
            if area[r][c]!=new_area[r][c]:
                stable = False            
    #print_area(count)
    return stable,new_area

print_area(area)
stable = False
while not stable:
    stable,area = iterate_area(area)
    print_area(area)
print(sum(line.count('#') for line in area))

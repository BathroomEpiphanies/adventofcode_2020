import sys
import json
from collections import defaultdict
from math import sqrt
from itertools import permutations
from copy import deepcopy
import numpy as np

count_shapes = defaultdict(lambda:0)

def print_tiles(tiles):
    for id_,tile in tiles.items():
        print(id_)
        print(tile['edges'][0])
        print(tile['edges'][1])
        print([count_shapes[i] for i in tile['edges'][0]])
        print()

#def print_tiles(tiles):
#    for id_,tile in tiles.items():
#        print(id_)
#        print(tile['edges'][0])
#        print([count_shapes[i] for i in tile['edges'][0]])
#        print(tile['edges'][1])
#        print([count_shapes[i] for i in tile['edges'][1]])
#        for row in tile['image']:
#            print(''.join(row))
#        print()

tiles = defaultdict(lambda:{})
input_ = (line.strip() for line in sys.stdin.readlines())
for line in input_:
    id_ = line[5:-1]
    
    tiles[id_]['image'] = []
    for line in input_:
        if not line: break
        tiles[id_]['image'].append(line)
    
    tiles[id_]['edges'] = [[None for _ in range(4)],[None for _ in range(4)]]
    edge = ''.join([col for col in tiles[id_]['image'][0]])
    tiles[id_]['edges'][0][0] = edge
    tiles[id_]['edges'][1][0] = edge[::-1]
    count_shapes[edge] += 1
    count_shapes[edge[::-1]] += 1
    edge = ''.join([row[-1] for row in tiles[id_]['image']])
    tiles[id_]['edges'][0][1] = edge
    tiles[id_]['edges'][1][3] = edge[::-1]
    count_shapes[edge] += 1
    count_shapes[edge[::-1]] += 1
    edge = ''.join([col for col in reversed(tiles[id_]['image'][-1])])
    tiles[id_]['edges'][0][2] = edge
    tiles[id_]['edges'][1][2] = edge[::-1]
    count_shapes[edge] += 1
    count_shapes[edge[::-1]] += 1
    edge = ''.join([row[0] for row in reversed(tiles[id_]['image'])])
    tiles[id_]['edges'][0][3] = edge
    tiles[id_]['edges'][1][1] = edge[::-1]
    count_shapes[edge] += 1
    count_shapes[edge[::-1]] += 1

print_tiles(tiles)

side = round(sqrt(len(tiles)))
#print(side)

product = 1
for id_,tile in tiles.items():
    if sum([count_shapes[i] for i in tile['edges'][0] if count_shapes[i]==1])==2:
        print(id_)
        product *= int(id_)
print(product)



board = {}
for i in range(side):
    board[-1+i*1j] = None
    board[i-1j] = None
print(board)
flips = {}
rotations = {}
solution = []
#used = {tile:False for tile in tiles}
#solution = ['1951','2311','3079','2729','1427','2473','2971','1489','1171']
#solution = ['1951','2311','3079','2729']
#solution = ['1951','2311']
#used = {tile:False for tile in solution}

used = {tile:False for tile in tiles}
def place_tile(pos):
    #print(used.values())
    if(all(used.values())): return True
    nextpos = (pos.real+1)%side + (pos.imag+(pos.real+1)//side)*1j
    #for this in tiles:
    #print(solution)
    for this in tiles:
        if used[this]: continue
        solution.append(this)
        used[this] = True
        #print(f'placing: {this}, in {pos}')
        board[pos] = this
        for flip in range(2):
            flips[this] = flip
            for rotation in range(4):
                rotations[this] = rotation
                that = board[pos-1j]
                check_top  = that is None or \
                             tiles[this]['edges'][flips[this]][(rotations[this]+0)%4] == \
                             tiles[that]['edges'][flips[that]][(rotations[that]+2)%4][::-1]
                that = board[pos-1]
                check_left = that is None or \
                             tiles[this]['edges'][flips[this]][(rotations[this]+3)%4] == \
                             tiles[that]['edges'][flips[that]][(rotations[that]+1)%4][::-1]
                #print([(o,flips[o],rotations[o]) for o in solution])
                #print(check_top,check_left)
                if check_left and check_top and place_tile(nextpos):
                    return True
        solution.pop()
        used[this] = False
    return False


success = place_tile(0)
print(success)
print(solution)

#solution = ['3931', '2251', '2833', '1321', '1123', '3881', '2539', '2999', '1931', '3709', '3499', '3323', '1913', '2687', '3701', '1201', '3617', '2039', '3299', '3511', '2819', '2897', '3727', '2203', '1009', '2239', '3469', '1997', '2179', '3739', '3217', '3559', '3943', '1669', '2423', '2243', '1823', '2347', '1621', '1429', '3919', '1847', '2621', '3557', '1277', '2131', '1019', '1663', '2927', '2657', '3257', '2137', '2749', '1093', '1493', '3457', '2879', '3719', '1471', '1733', '2837', '2693', '3467', '2129', '2851', '2293', '1109', '2803', '2339', '1213', '2593', '3779', '2081', '3301', '2549', '2957', '2309', '1801', '2371', '2029', '1867', '1697', '2477', '1789', '2617', '2953', '1367', '2843', '1297', '1459', '2383', '3613', '3019', '1051', '3923', '1129', '2153', '1091', '3391', '2551', '2711', '3329', '2729', '2647', '1303', '2557', '1753', '3517', '1223', '1511', '1097', '1483', '2521', '2017', '3527', '3677', '3581', '1907', '2381', '3659', '2719', '3529', '1031', '2437', '1229', '1447', '3373', '1579', '2887', '1777', '1999', '3169', '3343', '2609', '3413', '1453', '2267', '3989', '3803', '1283', '2143', '1451', '3313', '3221']

def print_image(image):
    print('\n'.join(image))
def flip_image(image):
    return [row[::-1] for row in image]
def rotate_image(image):
    return [''.join(row[col] for row in image) for col,_ in reversed(list(enumerate(image[0])))]

#print_image(tiles['1427']['image'])
#print()
#print_image(flip_image(tiles['1427']['image']))
#print()
#print_image(rotate_image(tiles['1427']['image']))
#print()

oriented_tiles = {}
for id_ in solution:
    oriented_tiles[id_] = deepcopy(tiles[id_]['image'])
    for _ in range(flips[id_]):
        oriented_tiles[id_] = flip_image(oriented_tiles[id_])
    for _ in range(rotations[id_]):
        oriented_tiles[id_] = rotate_image(oriented_tiles[id_])
    oriented_tiles[id_] = [row[1:-1] for row in oriented_tiles[id_][1:-1]]

image = []
for y in range(side):
    for r,_ in enumerate(oriented_tiles[solution[0]]):
        line = ''
        for x in range(side):
            line += oriented_tiles[solution[y*side+x]][r]
        image.append(line)

print_image(image)

sea_monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]
monster_size = sum([row.count('#') for row in sea_monster])
print(monster_size)
def test_moster(image,y,x):
    if y+len(sea_monster) > len(image):
        return False
    if x+len(sea_monster[0]) > len(image[0]):
        return False
    for r,row in enumerate(sea_monster):
        for c,col in enumerate(row):
            if sea_monster[r][c]=='#' and col!=image[y+r][x+c]:
                return False
    return True


total = sum([row.count('#') for row in image])
print(total)

monster_count = 0
for flip in range(2):
    if monster_count!=0: break
    for rotate in range(4):
        if monster_count!=0: break
        for r,row in enumerate(image):
            for c,_ in enumerate(row):
                if test_moster(image,r,c):
                    monster_count += 1
        image = rotate_image(image)
    image = flip_image(image)
    
print(monster_count)
print(total-monster_count*monster_size)

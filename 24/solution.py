import sys
from collections import defaultdict
from itertools import product

dirs = {'e':+1+0j,'ne':+1+1j,'nw':+0+1j,'w':-1+0j,'sw':-1-1j,'se': +0-1j}

flipped = defaultdict(lambda:False)
for line in (line.strip() for line in sys.stdin.readlines()):
    for d in ['ne','nw','se','sw','e','w']:
        line = line.replace(d,f'({dirs[d]})+')
    tile = eval(f'{line}0')
    flipped[tile] ^= True
flipped = {k for k,v in flipped.items() if v}
print(len(flipped))


def evolve(flipped):
    def neighbors(tile):
        return len([None for d in dirs.values() if tile+d in flipped])
    return {tile for tile in flipped if neighbors(tile) in [1,2]} |\
           {tile for tile in (t+d for t,d in product(flipped,dirs.values())) if tile not in flipped and neighbors(tile)==2}


for _ in range(100):
    flipped = evolve(flipped)
print(len(flipped))

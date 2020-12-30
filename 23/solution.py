import sys
import json


def play(cups,pos,mod):
    draw = [cups[pos],cups[cups[pos]],cups[cups[cups[pos]]]]
    #print(draw)
    cups[pos] = cups[draw[-1]]
    insert = (pos-1)%mod
    while insert in draw:
        insert = (insert-1)%mod
    #print(insert)
    cups[draw[-1]] = cups[insert]
    cups[insert] = draw[0]
    return cups,cups[pos]


def list_cups(cups,pos):
    start = pos
    output = [pos+1]
    pos = cups[pos]
    while pos != start:
        output.append(pos+1)
        pos = cups[pos]
    return output



input_ = list(int(n)-1 for n in sys.stdin.readline())
print(input_)


mod = len(input_)
cups = {}
for i in range(0,mod-1):
    cups[input_[i]] = input_[i+1]
cups[input_[-1]] = input_[0]

pos = input_[0]
for _ in range(100):
    print(list_cups(cups,pos))
    cups,pos = play(cups,pos,mod)
print(list_cups(cups,pos))
print(''.join(f'{n}' for n in list_cups(cups,0)[1:]))


mod = 1000000
cups = {i:i+1 for i in range(mod)}
for i in range(0,len(input_)-1):
    cups[input_[i]] = input_[i+1]
cups[input_[-1]] = len(input_)
cups[mod-1] = input_[0]
print(' '.join(map(str,list_cups(cups,input_[0])[:20])))
print(' '.join(map(str,list_cups(cups,input_[0])[-20:])))
print(cups[mod-1])

pos = input_[0]
for _ in range(10*mod):
    cups,pos = play(cups,pos,mod)
print(cups[0]+1,cups[cups[0]]+1,(cups[0]+1)*(cups[cups[0]]+1))

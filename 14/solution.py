import sys
import re
import json

#mask = sys.stdin.readline().strip().split(' = ')[1]
#mask0 =  int('0'*36,2) ^ int(mask.replace('X','1'),2)
#mask1 =  int(mask.replace('X','0'),2)
#
#operations = []
#for line in sys.stdin.readlines():
#    match = re.match('mem\[(?P<address>[0-9]+)\] = (?P<value>[0-9]+)',line).groupdict()
#    print(match)
#    operations.append(match)
#
#
#print(f'{mask:>36}')
#print(f'{mask0:036b}')
#print(f'{mask1:036b}')
#print(operations)
#
#
#memory = {}
#for op in operations:
#    memory[op['address']] = int(op['value']) & mask0 | mask1
#    print(op, memory[op['address']])
#
#print(sum( value for _,value in memory.items() ))

input_ = [line.strip() for line in sys.stdin.readlines()]



#memory = {}
#for line in input_:
#    if line[0:4] == 'mask':
#        mask = line.split(' = ')[1]
#        mask0 =  int('0'*36,2) ^ int(mask.replace('X','1'),2)
#        mask1 =  int(mask.replace('X','0'),2)
#        print(f'{mask:>36}')
#        print(f'{mask0:036b}')
#        print(f'{mask1:036b}')
#    elif line[0:3] == 'mem':
#        operation = re.match('mem\[(?P<address>[0-9]+)\] = (?P<value>[0-9]+)',line).groupdict()
#        memory[operation['address']] = int(operation['value']) & mask0 | mask1
#print(memory)        
#print(sum( value for _,value in memory.items() ))







memory = {}

def mem_write(address,mask,depth,value):
    if depth>35:
        memory[address] = value
    elif mask[depth] == 'X':
        mem_write(address[:depth]+'1'+address[depth+1:],mask,depth+1,value)
        mem_write(address[:depth]+'0'+address[depth+1:],mask,depth+1,value)
    elif mask[depth] == '1':
        mem_write(address[:depth]+'1'+address[depth+1:],mask,depth+1,value)
    else:
        mem_write(address,mask,depth+1,value)



for line in input_:
    if line[0:4] == 'mask':
        mask = line.split(' = ')[1]
        print(mask, mask.count('X'))
    elif line[0:3] == 'mem':
        operation = re.match('mem\[(?P<address>[0-9]+)\] = (?P<value>[0-9]+)',line).groupdict()
        mem_write(f'{int(operation["address"]):036b}',mask,0,int(operation['value']))

#print(json.dumps(memory,indent=4))
print(len(memory))
print(sum( value for _,value in memory.items() ))

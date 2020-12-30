import sys
import json
from copy import deepcopy

program = [line.strip().split(' ') for line in sys.stdin.readlines()]
#print(json.dumps(program,indent=4))

def run_program(program):
    accumulator = 0
    pointer = 0
    visited = set()
    while pointer<len(program) and pointer not in visited:
        visited.add(pointer)
        op,val = program[pointer]
        if op=='nop':
            pointer += 1
        elif op=='jmp':
            pointer += int(val)
        elif op=='acc':
            accumulator += int(val)
            pointer += 1
    return ('loop' if pointer<len(program) else 'halt',accumulator)

print(run_program(program))

for i in range(len(program)):
    tmp = deepcopy(program)
    if tmp[i][0] == 'nop':
        tmp[i][0] = 'jmp'
    elif tmp[i][0] == 'jmp':
        tmp[i][0] = 'nop'
    else:
        continue
    state,accumulator = result = run_program(tmp)
    if state=='halt':
        print(result)

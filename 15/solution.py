import sys
from copy import deepcopy

numbers = sys.stdin.readline().strip().split(',')
last_seen = {int(n):i for i,n in enumerate(numbers[:-1])}
next_number = int(numbers[-1])

interation = len(last_seen)
while True:
    if interation==2020:
        print(last_number)
    elif interation==30000000:
        print(last_number)
        break
    
    last_number = next_number
    if last_number in last_seen:
        next_number = interation - last_seen[last_number]
    else:
        next_number = 0
    
    last_seen[last_number] = interation
    interation += 1

import sys
from itertools import combinations

numbers = [int(line) for line in sys.stdin.readlines()]


for i in range(25,len(numbers)):
    if not any(map(lambda x: x==numbers[i],[a+b for a,b in combinations(numbers[i-25:i],2)])):
        number = numbers[i]
        print(i,numbers[i])

for i in range(len(numbers)):
    for j in range(i+2,len(numbers)):
        if sum(numbers[i:j])==number:
            print(numbers[i:j],min(numbers[i:j])+max(numbers[i:j]))

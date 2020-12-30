import sys

numbers = [int(x) for x in sys.stdin.readlines()]
print(numbers)

for x in numbers:
    for y in numbers:
        if x+y == 2020:
            print(f'{x} * {y} = {x*y}')

for x in numbers:
    for y in numbers:
        for z in numbers:
            if x+y+z == 2020:
                print(f'{x} * {y} * {z} = {x*y*z}')


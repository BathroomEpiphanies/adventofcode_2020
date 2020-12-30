import sys
import re

instructions = [re.match('(?P<move>.)(?P<amount>.*)',line).groupdict() for line in sys.stdin.readlines()]

position = 0+0j
moves = {
    'N': +1j,
    'S': -1j,
    'E': +1,
    'W': -1,
    'L': +1j,
    'R': -1j,
    'F': +1,
}
for instruction in instructions:
    if instruction['move'] in ['N','S','E','W','F']:
        position += moves[instruction['move']]*int(instruction['amount'])
    elif instruction['move'] in ['R','L']:
        moves['F'] *= moves[instruction['move']]**(int(instruction['amount'])//90)
print(int(abs(position.real)+abs(position.imag)))


heading = 10+1j
position = 0+0j
moves = {
    'N': +1j,
    'S': -1j,
    'E': +1,
    'W': -1,
    'L': +1j,
    'R': -1j,
}
for instruction in instructions:
    if instruction['move'] in ['N','S','E','W']:
        heading += moves[instruction['move']]*int(instruction['amount'])
    elif instruction['move'] in ['R','L']:
        heading *= moves[instruction['move']]**(int(instruction['amount'])//90)
    elif instruction['move'] in ['F']:
        position += heading*int(instruction['amount'])
print(int(abs(position.real)+abs(position.imag)))


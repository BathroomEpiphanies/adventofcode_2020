import sys
import re
from collections import deque
from itertools import count

input_ = (line.strip() for line in sys.stdin.readlines())

decks = [deque(),deque()]
for deck in decks:
    next(input_)
    for line in input_:
        if not line: break
        deck.append(int(line))


#print(decks)


def play_game(decks,previous):
    deck0,deck1 = decks
    while True:
        print(decks)
        if not deck0: return 1
        if not deck1: return 0
        
        setup = hash((tuple(deck0),tuple(deck1)))
        if setup in previous:
            return 0
        previous.add(setup)
        
        card0 = deck0.popleft()
        card1 = deck1.popleft()
        if len(deck0)<card0 or len(deck1)<card1:
            if card0 > card1:
                winner = 0
            else:
                winner = 1
        else:
            subdeck0 = deque(list(deck0)[:card0])
            subdeck1 = deque(list(deck1)[:card1])
            winner = play_game([subdeck0,subdeck1],set())
            
        if winner == 0:
            deck0.extend([card0,card1])
        else:
            deck1.extend([card1,card0])


winner = play_game(decks,set())
print(decks)
score = sum((card*value for card,value in zip(reversed(decks[winner]),count(1,1))))
print(winner)
print(score)


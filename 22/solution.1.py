import sys
import re
from collections import deque
from itertools import count

input_ = (line.strip() for line in sys.stdin.readlines())


decks = {}
for line in input_:
    if not line:
        continue
    else:
        match = re.match('^Player ([12]):$',line)
        if match:
            player = f'player{match.group(1)}'
            decks[player] = deque()
        else:
            decks[player].append(int(line))



print(decks)
while all(decks.values()):
    round_ = sorted([(deck.popleft(),player) for player,deck in decks.items()],reverse=True)
    winner = round_[0][1]
    cards = [card for card,_ in round_]
    decks[winner].extend(cards)
    print(round_,winner)
    print(decks)
    
score = sum((card*value for card,value in zip(reversed(decks[winner]),count(1,1))))
print(winner)
print(score)


import sys
import re

input_ = [line.strip() for line in sys.stdin.readlines()]

valid_count = 0
for line in input_:
    match = re.match('(?P<mincount>[0-9]+)-(?P<maxcount>[0-9]+) +(?P<letter>[a-z]): +(?P<password>[a-z]+)',line).groupdict()
    count = match['password'].count(match['letter'])
    if int(match['mincount']) <= count <= int(match['maxcount']):
        valid_count += 1
print(valid_count)


valid_count = 0
for line in input_:
    match = re.match('(?P<pos1>[0-9]+)-(?P<pos2>[0-9]+) +(?P<letter>[a-z]): +(?P<password>[a-z]+)',line).groupdict()
    a = match['password'][int(match['pos1'])-1]
    b = match['password'][int(match['pos2'])-1]
    c = match['letter']
    if (a==c and b!=c) or (a!=c and b==c):
        valid_count += 1
print(valid_count)

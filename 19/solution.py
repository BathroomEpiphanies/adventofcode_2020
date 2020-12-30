import sys
import re

rules = {}
while True:
    line = sys.stdin.readline().strip()
    if not line: break
    index,rule = line.split(': ')
    match = re.match('"[a-z]"',rule)
    if match:
        rules[index] = eval(match.group(0))
    else:
        options = rule.split(' | ')
        rules[index] = [option.split(' ') for option in options]

def build(rule):
    if type(rules[rule]) is not list:
        return rules[rule]
    else:
        return f'(?:{"|".join(["".join([build(i) for i in option]) for option in rules[rule]])})'
regex = f'^{build("0")}$'


messages = [line.strip() for line in sys.stdin.readlines()]


passed = 0
for line in messages:
    if re.match(regex,line):
        passed += 1
print(passed)


regex = regex.replace(build("42"),f'(?P<h1>({build("42")[3:-1]})+?)',1)
regex = regex.replace(build("42"),f'(?P<h2>({build("42")[3:-1]})+)',1)
regex = regex.replace(build("31"),f'(?P<h3>({build("31")[3:-1]})+)',1)

passed = 0
for line in messages:
    match = re.match(regex,line)
    if match:
        groups = match.groupdict()
        if len(groups['h2']) >= len(groups['h3']):
            passed += 1
print(passed)

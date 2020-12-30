import sys

input_ = [line.strip() for line in sys.stdin.readlines()]

sum_ = 0
for line in input_:
    sum_ += len(set(line)-set(' '))
print(sum_)

sum_ = 0
for group in input_:
    questions = set(map(chr,range(ord('a'),ord('z')+1)))
    for person in group.split(' '):
        questions = questions & set(person)
    sum_ += len(questions)
print(sum_)

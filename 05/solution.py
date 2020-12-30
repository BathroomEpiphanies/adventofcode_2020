import sys

ids = set(int(line.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2) for line in sys.stdin.readlines())
print(max(ids))
print(set(range(min(ids),max(ids)+1))-ids)

import sys
import re
from collections import defaultdict
from functools import reduce
import networkx


field_allows = defaultdict(lambda:set())
while True:
    line = sys.stdin.readline().strip()
    if len(line) == 0: break
    name,ranges = line.split(': ')
    for range_ in ranges.split(' or '):
        a,b = map(int,range_.split('-'))
        field_allows[name].update(range(a,b+1))
sys.stdin.readline()
myticket = list(map(int,sys.stdin.readline().split(',')))
sys.stdin.readline()
sys.stdin.readline()
tickets = [myticket]
for line in sys.stdin.readlines():
    tickets.append(list(map(int,line.split(','))))


all_allowed = reduce(lambda a,b:a|b,field_allows.values())

sum_ = 0
for i,ticket in reversed(list(enumerate(tickets))):
    for val in ticket:
        if val not in all_allowed:
            sum_ += val
            del(tickets[i])
            break
print(sum_)


graph = networkx.Graph()
for i,_ in enumerate(myticket):
    values = set(ticket[i] for ticket in tickets)
    for field,allowed in field_allows.items():
        if not values-allowed:
            graph.add_edge(i,field)
#match = networkx.algorithms.bipartite.matching.hopcroft_karp_matching(graph)
match = networkx.algorithms.bipartite.matching.maximum_matching(graph)

product = 1
for i,_ in enumerate(myticket):
    print(i,match[i])
    if re.search('^departure.*',match[i]):
        product *= myticket[i]
print(product)

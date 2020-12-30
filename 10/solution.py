import sys
from collections import defaultdict
from functools import cache

adapters = sorted(int(line) for line in sys.stdin.readlines())
adapters.append(adapters[-1]+3)
print(adapters)


diffs = defaultdict(lambda:0)
for i in range(1,len(adapters)):
    diffs[adapters[i]-adapters[i-1]] += 1

print(diffs)
print(diffs[1]*diffs[3])



import networkx as nx
import matplotlib.pyplot as plt
import graphviz as gv
from networkx.drawing.nx_agraph import graphviz_layout

connections = nx.DiGraph()
for adapter in adapters:
    for i in range(1,4):
        if adapter-i in adapters:
            connections.add_edge(adapter,adapter-i)


@cache
def combinations(adapter):
    return max(1,sum(combinations(previous) for previous in connections.successors(adapter)))

print(combinations(adapters[-1]))


#if True:
#    graphpos = graphviz_layout(connections)
#    nx.draw(connections,graphpos,node_size=400,node_color='#AADDDD')
#    nx.draw_networkx_labels(connections,graphpos,{n:f"{n}" for n in connections.nodes()},font_size=10)
#    nx.drawing.nx_pydot.write_dot(connections,"debug.dot")
#    plt.show()

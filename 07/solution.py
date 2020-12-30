import sys
import re
from collections import defaultdict

import networkx as nx
import matplotlib.pyplot as plt
import graphviz as gv
from networkx.drawing.nx_agraph import graphviz_layout

input_ = [line.strip() for line in sys.stdin.readlines()]

bags = nx.DiGraph()
for line in input_:
    tokens = line.split(', ')
    for token in tokens[1:]:
        match = re.search('(?P<count>[0-9]+) (?P<color>.*)',token).groupdict()
        bags.add_edge(tokens[0],match['color'],count=int(match['count']))

if len(bags.nodes())<100:
    graphpos = graphviz_layout(bags)
    nx.draw(bags,graphpos,node_size=400,node_color='#AADDDD')
    nx.draw_networkx_labels(bags,graphpos,{n:f"{n}" for n in bags.nodes()},font_size=10)
    nx.draw_networkx_edge_labels(bags,graphpos,{(u,v):d['count'] for (u,v,d) in bags.edges(data=True)})
    nx.drawing.nx_pydot.write_dot(bags,"debug.dot")
    plt.show()


outer_bags = nx.ancestors(bags,'shiny gold')
if len(bags.nodes())<100: print(outer_bags)
print(len(outer_bags))



def bag_contents(bag):
    return 1 + sum(bags.get_edge_data(bag,inner)['count'] * bag_contents(inner) for inner in bags.successors(bag))

print(bag_contents('shiny gold') - 1)

import sys
import re
import networkx


products = []
ingredients = set()
allergens = {}
for line in (line.strip() for line in sys.stdin.readlines()):
    ingredients_,allergens_ = re.match('^(.*) \(contains (.*)\)$',line).groups()
    ingredients_ = set(ingredients_.split(' '))
    allergens_ = allergens_.split(', ')
    products.append(ingredients_)
    for allergen in allergens_:
        if allergen in allergens:
            allergens[allergen] &= ingredients_
        else:
            allergens[allergen]  = ingredients_.copy()
    ingredients |= ingredients_


graph = networkx.Graph()
for allergen,ingredients_ in allergens.items():
    for ingredient in ingredients_:
        graph.add_edge(allergen,ingredient)
match = networkx.algorithms.bipartite.matching.maximum_matching(graph,allergens)
unsafe = {i:a for i,a in match.items() if i in ingredients}
safe = set(ingredients - unsafe.keys())


sum_ = 0
for product in products:
    sum_ += len(safe & product) 
print(sum_)
print(','.join([i for a,i in sorted([(a,i) for i,a in unsafe.items()])]))

import networkx as nx
from networkx.algorithms import bipartite
from collections import Counter
import random 
import matplotlib.pyplot as plt
f = open("ErdosRenyi.txt", "r")

G = nx.Graph()
k = 10
hub = Counter()
authority = Counter()
lines = f.readlines()
# print(lines)

for line in lines:
    line = line.rstrip("\n")
    line = line [1:-1]
    line = line.split(', ')
    print(line)
    G.add_node(line[0])
    G.add_node(line[1])
    G.add_edge(line[0],line[1])    
    # "Making node "+ str(i)+ "/" +str(num_lines), end="\r", flush=True)

print("made graph")
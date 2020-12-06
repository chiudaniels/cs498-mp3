import networkx as nx
# from networkx.algorithms import bipartite
from collections import Counter
import random 


#betweenness loop 
# bfs is queue. use append and pop
#betweenness loop 
# bfs is queue. use append and pop
def updateBetweenness(graph_list):     
    max_edge_val = 0
    maxEdge = (0,0)
    partition_count = 0
    for graph in graph_list:
        nodes = list(graph.nodes())
        # print(nodes)
        i = 0
        for node in nodes:
            y = 0
            prevSteps = {}
            tree = list(nx.bfs_tree(graph,node).edges())
            # print(node)
            # print(list(nx.bfs_tree(graph,node).edges()))                
            for edge in tree:
                prev_edge = []
                if edge[0] in prevSteps:
                    prev_edge = prevSteps[edge[0]]
                prev_edge.append(edge)
                for update_edge in prev_edge:
                    graph[update_edge[0]][update_edge[1]]["flow"] += 1
                prevSteps[edge[1]] = prev_edge
                y += 1
            print("partition: "+ str(partition_count)+"/"+str(len(graph_list))+ "    updated " + str(i) + "/"+ str(len(nodes)), end="\r")
            i += 1 

        # print(list(graph.edges().data()))
        for edge in graph.edges():
            if graph[edge[0]][edge[1]]["flow"] > max_edge_val:
                max_edge_val =graph[edge[0]][edge[1]]["flow"]
                maxEdge = edge
        partition_count += 1
    
    print("")
    # print("\n done updating")
    # return maxEdge           
            
def findMax(graph_list):
    max_edge_val = 0
    maxEdge = (0,0)
    for graph in graph_list:
        for edge in graph.edges():
            if graph[edge[0]][edge[1]]["flow"] > max_edge_val:
                max_edge_val =graph[edge[0]][edge[1]]["flow"]
                maxEdge = edge
    return maxEdge           
            
def deleteEdge(graph_list, del_edge):
    for graph in graph_list:
        for edge in graph.edges():
            if del_edge == edge:
                graph.remove_edge(edge[0],edge[1])


def findModularity(graph):
    modul = 0
    total_edges = len(graph.edges())
    for vertex1 in graph.nodes:
        for vertex2 in graph.nodes:
        # for neighbor in graph.neighbors(vertex):
            if vertex1 == vertex2:
                continue
            edge = (vertex1, vertex2)
            rev_edge = (vertex2, vertex1)
            adj = 0
            if edge in graph.edges() or rev_edge in graph.edges():
                adj = 1
            i_deg = len(graph.edges(vertex1))
            j_deg = len(graph.edges(vertex2))
            # actual = i_deg + j_deg
            expected = (i_deg * j_deg) / (2*total_edges)
            modul += adj - expected
    return modul / (2*total_edges)


# import matplotlib.pyplot as plt
f = open("ErdosRenyi.txt", "r")
# f = open("Barabasi.txt", "r")
# f = open("WattsStrogatz.txt", "r")
# f = open("test.txt", "r")
G = nx.Graph()
shortest_paths = {}
# print(lines)
lines = f.readlines()

for line in lines:
    line = line.rstrip("\n")
    line = line [1:-1]
    line = line.split(', ')
    G.add_node(line[0])
    G.add_node(line[1])
    G.add_edge(line[0],line[1], flow = 0)    

m = len(G.edges())
S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
print("inital mod")
print(findModularity(G))
print("0 edges removed")

edges_removed = 0
currLen = 1
while len(S) != 5: 
    updateBetweenness(S)
    while (len(list(nx.connected_components(G))) == currLen): 
        highest_bet = findMax(S)
        deleteEdge(S, highest_bet)
        edges_removed += 1
        G.remove_edge(highest_bet[0], highest_bet[1])
   
    S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
    currLen = len(S)
    print(str(currLen) +" partitions")
    print(str(edges_removed) + " edges removed")
    print("modularity: "+ str(findModularity(G)))
    # if len(S) != currLen:
    #     currLen = len(S)
    #     print(str(currLen) +" partitions")
    #     print(str(edges_removed) + " edges removed")
    #     print("modularity: "+ str(findModularity(G)))
    

# print(findModularity(G))
# for graph in S:
#     print(findModularity(graph))
    
#calculate initial modularity
# init_mod = findModularity(G)

# updateBetweenness(G)



    
# print("made graph")
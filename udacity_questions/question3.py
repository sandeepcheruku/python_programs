
"""
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects 
all vertices in a graph with the smallest possible total weight of edges. 
Your function should take in and return an adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}

Vertices are represented as unique strings. The function definition should be question3(G)
"""

# To keep track of vertices and their ranks  
parent = dict()
rank = dict()

# Makes a set 
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

# Helper function to find connection, used for finding cycles  
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

# Function that does union of two sets a,b
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        # Attaching smaller rank tree under root of high rank tree
        if rank[root1] > rank[root2]: 
           parent[root2] = root1
        else:
            parent[root1] = root2
            #If ranks are same, then make one of them as root and increment
            if rank[root1] == rank[root2]: rank[root2] += 1


# returns MST of a graph; uses kruskal's algorithm 
def kruskal(graph):

    # creates subsets equal to no of vertices
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort() # sorts edges in decreasing order of weights
    for edge in edges:
        weight, vertice1, vertice2 = edge
        # Verifies if including this edge causes a cycle, if not adds to result; moves to next edge 
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree

# Helper function for format_graph()
def is_edge_present(edges,edge):
    for temp in edges:
        if temp[0] == edge[0]:
           if temp[1] == edge[2] and temp[2] == edge[1]:
              return 1
    return 0
    
# extracts the edges from input graph
def format_graph(graph):
    mod_graph = {}
    nodes = []
    edges = []
    for i in graph:
        nodes.append(i)
        for j in graph[i]:
            edge = tuple(reversed(j)) + tuple(i)
            if not is_edge_present(edges,edge):
               edges.append(edge)
    mod_graph['vertices'] = nodes
    mod_graph['edges'] = set(edges)
    return mod_graph    

# returns graph in adjacency list notation 
def reformat_graph(graph):
    g1 ={}
    for edge in graph:
        if edge[1] not in g1:
           g1[edge[1]] = []
        if edge[2] not in g1:
           g1[edge[2]] = []
        temp1 = []
        temp1.append(edge[2])
        temp1.append(edge[0])
        temp1 = tuple(temp1)
        temp2 = []
        temp2.append(edge[1])
        temp2.append(edge[0])
        temp2 = tuple(temp2)
        g1[edge[1]].append(temp1)
        g1[edge[2]].append(temp2)
    return g1

# returns Minimum spanning tree of input graph using kruskal's algorithm 
def question3(graph):
    mod_graph = format_graph(graph) 
    mst = kruskal(mod_graph)
    mst = reformat_graph(mst)
    return mst

if __name__ == "__main__":

    #case 1:
    graph = {'A': [('B', 2), ('C',1)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
    # expected = {'A': [('C', 1), ('B', 2)], 'C': [('A', 1)], 'B': [('A', 2)]}
    print question3(graph)
   
    #case 2:
    graph = {'A': [('B', 1), ('C',-1), ('D',2)], 'B': [('A', 1), ('C',1), ('D',3)], 'C': [('A', -1),('B',1)], 'D':[('A',2), ('B',3)]}
    # expected = {'A': [('B', 1), ('D', 2), ('C', -1)], 'C': [('A', -1)], 'B': [('A', 1)], 'D': [('A', 2)]}
    print question3(graph)

    #case 3:
    graph = {'A': [('B', 2), ('C',-1),('D',4)], 'B': [('A', 2), ('C', 1),('D',3)], 'C': [('B', 1),('D',5),('A',-1)], 
             'D':[('A',4),('B',3),('C',5)]}
    # expected = {'A': [('C', -1)], 'C': [('A', -1), ('B', 1)], 'B': [('D', 3), ('C', 1)], 'D': [('B', 3)]}
    print question3(graph)

"""
Complexity :
E = no of edges 
V = no of vertices 
For sorting the edges : O(ElogE)
each find and union take : O(logV)
for E edges = O(ElogV)
total = O(ElogE) + O(ElogV) 
E can be = V^2 
so, worst case = ElogE or ElogV 
"""


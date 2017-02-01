
#-------------------------------------------------------------------------------#
# question 1

# this program verfies by measuring the frequencies of the substrings 
def question1(s,t):

    freq_p = [0] * 256
    freq_t = [0] * 256
    len_t = len(s)
    len_p = len(t)

    if len_p > len_t:
       return False

    for i in range(len_p):
        freq_t[ord(s[i])] +=1
        freq_p[ord(t[i])] +=1

    for i in range(len_p,len_t):
        if freq_p == freq_t:
           return True
        freq_t[ord(s[i-len_p])] -=1
        freq_t[ord(s[i])] +=1

    if freq_p == freq_t:
       return True
    else:
       return False

#----------------------------------------------------------------------------------#
# question-2

def is_palindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True

def substrings(word):
    tmp = []
    length = len(word)
    for i in range(length):
        for j in range(i,length):
               tmp.append(word[i:j+1])
    return tmp 

def question2(word):
    long_palind = ""
    length = len(long_palind)
    substring_list = substrings(word)
    for i in substring_list:
        if is_palindrome(i):
           if length < len(i):
              long_palind = i
              length = len(i)
    return long_palind
#-----------------------------------------------------------------------------------#
# question3

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
#-----------------------------------------------------------------------------------#
# question-4

def get_right_child(T1,r):
    tmp = T1[r]
    for i,val in enumerate(tmp):
        if val == 1:
           index = i

    if index > r:
       return index
    else:
       return None

def get_left_child(T1,r):
    tmp = T1[r]
    for i,val in enumerate(tmp):
        if val == 1:
           if i < r :
              return i
           else:
              return None

# the function that finds the least common ancestor (LCA) 
def question4(T1,r,p,q):
    # print get_right_child(T1,r)
    # print get_left_child(T1,r)

    a, b = sorted([p, q])
    while not a <= r <= b:
          # Keep searching since root is outside of [a, b].
          r = get_left_child(T1,r) if a <= r else get_right_child(T1,r)
    # a <= root.val <= b.
    return r

#-----------------------------------------------------------------------------------#
# question-5

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    # returns the no of elements in linkedlist 
    def length(self):
        temp = self.head 
        length = 0
        while temp:
           length += 1
           temp = temp.next 
        return length 

    def display(self):
        temp = self.head
        while temp:
            print temp.value
            temp = temp.next

def question5(ll,m):
    
    # taking care of corner case 
    if m <=0 :
       return None

    l = ll.length()
    position = l-m+1 
    count = 1
    tmp = ll.head

    # reading from requested position 
    if not 0 < position < l+1:
        return None
    else: 
       while tmp:
             if count == position:
                return tmp.value
             count += 1
             tmp = tmp.next 

#-----------------------------------------------------------------------------------#

if __name__ == "__main__":

    #question-1 :
    print "question-1 answers :"
    print question1("udacity","ad")
    # expected ans : True
    print question1("python","hno")
    # expected ans : True
    print question1("california","lya")
    # expected ans : False

    #question-2:
    print ""
    print "question-2 answers :"
    print question2("agodsawIwasdogb")
    # expected ans : 'godsawIwasdog'
    print question2("madam")
    # expected ans : 'madam'
    print question2("a")
    # expected ans : 'a'
    print question2("ebcdef")
    # expected ans : 'e'

    #question-3:
    print ""
    print "question-3 answers :"
    #case 1:
    graph = {'A': [('B', 2), ('C',1)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
    print question3(graph)
    # expected = {'A': [('C', 1), ('B', 2)], 'C': [('A', 1)], 'B': [('A', 2)]}
    #case 2:
    graph = {'A': [('B', 1), ('C',-1), ('D',2)], 'B': [('A', 1), ('C',1), ('D',3)], 'C': [('A', -1),('B',1)], 'D':[('A',2), ('B',3)]}
    print question3(graph)
    # expected = {'A': [('B', 1), ('D', 2), ('C', -1)], 'C': [('A', -1)], 'B': [('A', 1)], 'D': [('A', 2)]}
    #case 3:
    graph = {'A': [('B', 2), ('C',-1),('D',4)], 'B': [('A', 2), ('C', 1),('D',3)], 'C': [('B', 1),('D',5),('A',-1)], 
             'D':[('A',4),('B',3),('C',5)]}
    print question3(graph)
    # expected = {'A': [('C', -1)], 'C': [('A', -1), ('B', 1)], 'B': [('D', 3), ('C', 1)], 'D': [('B', 3)]}

    #question-4:
    print ""
    print "question-4 answers :"
    
    T1 =  [[0, 1, 0, 0, 0],   #input format example 
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]]

    print question4(T1,3,1,4) 
    # expected ans is '3'
    
    T2 =[[0, 0, 0, 0, 0, 0, 0], #root is '4'
         [0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0]]

    print question4(T2,4,2,3)
    # expected '2' 
    print question4(T2,4,3,6)
    # expected '4' 

    #question-5:
    print ""
    print "question-5 answers :"
    
    print "creating a linked list"
    e1 = Element(1)
    l1 = LinkedList(e1)
    for i in range(2,11):
       e1 = Element(i)
       l1.append(e1)
    print "creation done" 
    print question5(l1,3)    
    # expected ans is '8'
    print question5(l1,10)    
    # expected ans is '1'
    print question5(l1,-1)    
    # expected ans is 'None'
    print question5(l1,1)    
    # expected ans is '10'
    print question5(l1,0)    
    # expected ans is 'None'
    print question5(l1,11)    
    # expected ans is 'None'


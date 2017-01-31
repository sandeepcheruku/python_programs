
"""
Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is an ancestor of both nodes. 
For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, 
then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, 
and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), 
where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node 
and a 1 represents a child node, r is a non-negative integer representing the root, and 
n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
the answer would be :3 
"""

# node of a tree
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    
    def __init__(self, root):
        self.root = Node(root)

    # fun to insert an element in BST
    def insert(self, new_val):
        new_node = Node(new_val) 
        temp = self.root 
        prev = self.root

        while temp:
              if new_val > temp.value:
                 prev = temp
                 temp = temp.right
              else:
                 prev = temp
                 temp = temp.left 

        if new_val > prev.value:
           prev.right = new_node
        else:
            prev.left = new_node

    # traverses the tree in pre-order 
    def print_tree(self):
        return self.preorder_print(self.root, "")[:-1]

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    # returns the node which is the Least common ancestor  
    def lca(self,p,q):
        root = self.root
        a, b = sorted([p, q])
        while not a <= root.value <= b:
            # Keep searching since root is outside of [a, b].
            root = root.left if a <= root.value else root.right
        # a <= root.val <= b.
        return root
    
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

def lca(T1,r,p,q):
    # print get_right_child(T1,r)
    # print get_left_child(T1,r)

    a, b = sorted([p, q])
    while not a <= r <= b:
          # Keep searching since root is outside of [a, b].
          r = get_left_child(T1,r) if a <= r else get_right_child(T1,r)
    # a <= root.val <= b.
    return r

# builds the BST tree from matrix notation, 'r' indicates the value of the root 
def build_tree(T1,r):
    tree = BST(r)
    tmp = T1[r]
    to_visit = []
    to_visit.append(r)
  
    while len(to_visit):
          tmp = T1[to_visit[0]]
          to_visit.remove(to_visit[0])
          i=0
          while i < len(tmp):
                if tmp[i] == 1:
                   tree.insert(i)   
                   to_visit.append(i)
                i += 1
    return tree


if __name__ == "__main__":

    T1 =  [[0, 1, 0, 0, 0],   #input format example 
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]]

    T2 =[[0, 0, 0, 0, 0, 0, 0], #root is '4'
         [0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0]]

    print "using the function which just uses the input   "
    print "lca is :", lca(T1,3,1,4)
    # expected ans is '3'
    
    print "lca is :",lca(T2,4,2,3)
    # expected '2' 
    print "lca is :",lca(T2,4,3,6)
    # expected '4' 

    print "using the function which builds a BST from the input given "
    bst = build_tree(T1,3)
    print "pre-order traversal of tree is :"
    print bst.print_tree()
    
    # expected ans is '3'
    x1 = bst.lca(1,4)
    print "the least common ancestor of give inputs is :", x1.value

    
    bst = build_tree(T2,4)
    print bst.print_tree()
   
    # expected '2' 
    x1 = bst.lca(2,3)
    print "lca is :",x1.value     
    
    # expected '4' 
    x1 = bst.lca(3,6)
    print "lca is :",x1.value     

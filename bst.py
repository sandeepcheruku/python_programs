
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

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
           
    def search(self, find_val):
        temp = self.root
        while temp:
              if find_val == temp.value:
		 return True
              elif find_val > temp.value:
                   temp = temp.right
              else:
                   temp = temp.left
        return False

    def print_tree(self):
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

#print tree.print_tree()
# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

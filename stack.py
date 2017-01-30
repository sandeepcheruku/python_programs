
"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        new_element.next = self.head
        self.head = new_element 
        return "DONE"
    
    def delete(self):
        """Delete the first node with a given value."""
        if self.head == None:
           return "NONE"
        val = self.head.value
        self.head = self.head.next
        return val

    def display(self):
        temp = self.head
        while temp:
            print temp.value
            temp = temp.next


class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.append(new_element)
        
    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        val = self.ll.delete()
        return val

    def display(self):
        print "the stack is "
        self.ll.display()
   
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print stack.pop()
print stack.pop()
print stack.pop()
print stack.pop()
stack.push(e4)
print stack.pop()



"""
Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, 
the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), 
where ll is the first node of a linked list and m is the "mth number from the end". 
You should copy/paste the Node class below to use as a representation of a node in the linked list. 
Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
"""

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

    def display(self):
        temp = self.head
        while temp:
            print temp.value
            temp = temp.next

def question5(ll,m):
    current = ll.head
    tmp = []
    
    if ll.head == None: #to handle empty linked list
       return None  
    else:
        while current:
              tmp.append(current.value)
              current = current.next

    l = len(tmp)
    return tmp[l-m]


if __name__ == "__main__":

   print "creating a linked list"
   e1 = Element(10)
   l1 = LinkedList(e1)

   for i in range(1,5):
       e1 = Element(i)
       l1.append(e1)

   print "the linked list is :"
   l1.display()
   print "result is :",question5(l1,3)

     

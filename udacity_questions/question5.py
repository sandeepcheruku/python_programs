
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

# this method uses an additional list.So space and complexity are both O(n)
def question5(ll,m):
    current = ll.head
    tmp = []

    if m <=0 :
       return None

    if ll.head == None: #to handle empty linked list
       return None
    else:
        while current:
              tmp.append(current.value)
              current = current.next

    l = len(tmp)
    if l-m < 0:
       return None
    else:
       return tmp[l-m]


# this method does not use any additonal memory, but traverses the linkedlist twice
# Here time complexity is O(n), where as space complexity is O(1)
def question5_1(ll,m):

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
 

if __name__ == "__main__":

   print "creating a linked list"
   e1 = Element(1)
   l1 = LinkedList(e1)
   for i in range(2,11):
       e1 = Element(i)
       l1.append(e1)
  
   print "creation done"
   print "the linked list is :"
   l1.display()
   
   print " using the function which has time and space complexity of O(n)"  
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
  
   print " using the function which has space complexity O(1)"  
   print question5_1(l1,3)
   # expected ans is '8'
   print question5_1(l1,10)
   # expected ans is '1'
   print question5_1(l1,-1)
   # expected ans is 'None'
   print question5_1(l1,1)
   # expected ans is '10'
   print question5_1(l1,0)
   # expected ans is 'None'
 
   print "THE END" 

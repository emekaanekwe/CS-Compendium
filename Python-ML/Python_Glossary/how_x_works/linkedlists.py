'''
In Python, there is not inherent linked list DS. So,
it has to be made.
'''

class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data

#every LL requires a head
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    #since the element are dependent upon each other, if
        #the head is empty, then there is no LL
    def checkEmpty(self):
        if self.head is None:
            print("empty linked list")
            return self.head is None
            
    def appendNode(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        self.head = node
        
    
    def prepend(self, data):
        if self.head is None:
            print("cannot prepend empty Linked List")
            return 0
        for i in self.head:
            i.append(Node(data))
    #a list where a-b-c
    #and a points to be in list, i.e. a.get() -> b?
    
    
if "__main__" == __name__:
    Node
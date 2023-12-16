'''
Python does not have a built-in linked list DS. 

##Psuedocode
    1. LL has a starting point and end point
    2. create a node that must refer to some other node, otherwise not a LL
    3. doubly - each node must refer to a "previous node" and a "following node"
    4. each node can store a data type (uni or mult?)
    5. create core methods to operate on LL
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        
class Linked_List: 
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        
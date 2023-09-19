'''class Node:
    def __init__(self, data) -> None:
         self.data = data
         self.next = None'''
Node = []
head = None
next = None
def append(data):
    new_node = Node(data)
    if head is None:
        head = new_node
        return

    while next is None:
        current = next
    current = new_node
x = 'we\'re #2'
print(x)
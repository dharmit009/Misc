class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def countNodes(head):
    out = 0 
    if head.next == None: 
        return out
    else: 
        out += 1
    return out;

sixth  = Node(6, None)
fifth  = Node(5, sixth)
fourth = Node(4, fifth)
third  = Node(3, fourth)
second = Node(2, third)
first  = Node(1, second)

print("The Number of nodes the linked list has is equal to:" ,countNodes(third));


'''This is an example of linked list with only one element
    If we wanted to create an emplty LL we could have
    put None value in self.head and self.tail
    '''


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

new_linked_list = LinkedList(10)
print(new_linked_list.length)
print(new_linked_list.head.value)



class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        
        return result

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepand(self,value):
        new_node = Node(value)
        if self.head is None:
             self.head = new_node
             self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1

    def insert(self,index,value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            tmp_node = self.head
            for _ in range(index-1):
                tmp_node = tmp_node.next

            new_node.next = tmp_node.next
            tmp_node.next = new_node
        self.length += 1
        return True

    
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.prepand(5)
new_linked_list.insert(9,15)
new_linked_list.insert(0,0)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)
print(new_linked_list.length)
print(new_linked_list)
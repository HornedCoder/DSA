class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)
    
class Double_linked_list:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def __str__(self):
        result = ''
        temp = self.head
        while temp:
            result+= str(temp.value)
            if temp.next is not None:
                result += '<->'
            temp = temp.next
        return result

    def prepand(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

#   The following get method is optimised as it gets the value in n/2 T.C. Overall its basically O(n) T.C.
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if index < (self.length//2):
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length-1,index,-1):
                current = current.prev
        return current
        
    def set(self,index,value):
        node = self.get(index)
        if node is not None:
            node.value = value
            return True
        return False

    def insert(self,index,value):
        new_node = Node(value)
        if index<0 or index > self.length:
            print("index out of bounds")
            return
        if index == 0:
            self.prepand(value)
        elif index == self.length:
            self.append(value)
        else:
            prev_node = self.get(index-1)
            new_node.next = prev_node.next
            new_node.prev = prev_node
            prev_node.next.prev = new_node
            prev_node.next = new_node
        self.length += 1

    def pop_first(self):
        if self.head is None:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.head is None:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        
        self.length -= 1
        return popped_node

    def remove(self,index):
        if index < 0 or index >= self.length:
            return  None

        if index == 0:
            self.pop_first()
        elif index == self.length-1:
            self.pop()
        else:
            popped_node = self.get(index)
            prev_node = popped_node.prev
            prev_node.next = popped_node.next
            popped_node.next.prev = prev_node
            popped_node.next = popped_node.prev = None
            self.length -= 1
            return popped_node

dll = Double_linked_list()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepand(0)
dll.insert(2,8)
print(dll)
print(dll.get(1))
dll.set(1,9)
print(dll)
dll.pop_first()
print(dll)
dll.pop()
print(dll)
dll.remove(1)
print(dll)
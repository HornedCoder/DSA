class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return(str(self.value))

class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def __str__(self):
        result = ''
        current = self.head
        while current:
            result += str(current.value)
            if current.next == self.head:
                break
            result += '<->'
            current = current.next
        return result
    
    def prepand(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.head.prev = new_node
            self.tail.next = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            self.head = new_node
        self.length += 1

    def get(self,index):
        if index < 0  or index >= self.length:
            return "Out of index"
        
        if index < self.length//2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length-1,index,-1):
                current = current.prev
        
        return current
    
    def set(self,index,value):
        if index < 0 or index >= self.length:
            return "Index out of range"
        
        temp = self.get(index)
        if temp:
            temp.value = value
        
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return "Index out of range"
        
        new_node = Node(value)
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

    def pop(self):
        if self.length == 0:
            return None
        
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            popped_node.prev.next = self.head
            self.tail = popped_node.prev
            self.head.prev = self.tail
            popped_node.next = popped_node.prev = None

        self.length -= 1
        return popped_node
    
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            popped_node.next.prev = self.tail
            self.head = popped_node.next
            self.tail.next = self.head
            popped_node.next = popped_node.prev = None

        self.length -= 1
        return popped_node
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return "Index out of range"
        
        popped_node = self.get(index)
        if  index == 0:
            self.pop_first()
        elif index == self.length-1:
            self.pop()
        else:
            popped_node.prev.next = popped_node.next
            popped_node.next.prev = popped_node.prev
            popped_node.next = popped_node.prev = None
        
        self.length -= 1
        return popped_node


Cdll = CircularDoubleLinkedList()
Cdll.append(5)
Cdll.append(10)
Cdll.prepand(0)
print(Cdll)
print(Cdll.get(2))
Cdll.set(2,100)
Cdll.insert(3,50)
print(Cdll)
print(Cdll.pop())

print(Cdll)

print(Cdll.pop_first())

print(Cdll)
print(Cdll.remove(0))
print(Cdll)
print(Cdll.length)
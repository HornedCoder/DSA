class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
#This function is important as it is causing the iteration among the LL.
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
        
    def push(self,value):
        node = Node(value)
        if self.LinkedList.head is None:
            self.mini = value
        else:
            if self.mini > node.value:
                self.mini = node.value
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def minimum(self):
        return self.mini
    
    def pop(self):
        if self.isEmpty():
            return "There are  no elements present."
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return "There are  no elements present."
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
        
    def delete(self):
        self.LinkedList.head = None

s = Stack()
#print(s.isEmpty())
s.push(1)
s.push(2)
s.push(0)
s.push(4)
s.push(5)
print(s)
print("Min:",s.minimum())

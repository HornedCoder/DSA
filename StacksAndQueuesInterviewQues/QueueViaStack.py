class Stack():
    def __init__(self):
        self.list = []

    def __str__(self):
        return str(self.list)
    
    def __len__(self):
        return len(self.list)
    
    def push(self,value):
        self.list.append(value)

    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list.pop()
        
class QueStack():
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def __str__(self):
        return str(self.inStack)

    def enque(self,item):
        self.inStack.push(item)
    
    def deque(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result
    
s = QueStack()
s.enque(1)
s.enque(2)
s.enque(3)
s.deque()
print(s)
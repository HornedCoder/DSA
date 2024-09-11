class Stack_plates():
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return str(self.stacks)
    
    def push(self,item):
        if self.stacks == []:
            self.stacks.append([item])
        else:
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)

    def pop(self):
        if self.stacks == []:
            return "Stack is empty."
        popped_node = self.stacks[-1][-1]
        if len(self.stacks[-1]) == 1:
            del self.stacks[-1]
        else:
            del self.stacks[-1][-1]
        return popped_node
    
    def pop_at(self,stackNum):
        if len(self.stacks[stackNum]) > 0:
            return self.stacks[stackNum].pop()
        else:
            return None
    
s = Stack_plates(3)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.pop_at(1)
print(s)
#Use a single List to Implement three stacks.

class MultiStack:
    def __init__(self, stacksize):
        self.numberstacks = 3
        self.custList = [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks    #This creates another list which stores size of the stack.
        self.stacksize = stacksize

    def __str__(self):
        return str(self.custList)

    def isFull(self, stackNumber):  #This stackNumber parameter is taken to identify which stack we are talking about as there are 3 stacks.
        if self.sizes[stackNumber] == self.stacksize:
            return True
        else:
            return False
        
    def isEmpty(self, stackNumber):
        if self.sizes[stackNumber] == 0:
            return True
        else:
            return False
        
    #The following is a helper function which helps in returning the topIndex of the mentioned Stack.
    def topOfIndex(self, stackNumber):
        offset = stackNumber * self.stacksize
        return offset + self.sizes[stackNumber] - 1
    
    def push(self, items, stackNumber):
        if self.isFull(stackNumber):
            return "The Stack is Full"
        else: 
            self.sizes[stackNumber] += 1
            top = self.topOfIndex(stackNumber)
            self.custList[top] = items    #This might get wrong later as in tutorial video no +1 is being done. Tutorial was right. No +1 needed.

    def pop(self, stackNumber):
        if self.isEmpty(stackNumber):
            return "No item to pop."
        else:
            value = self.custList[self.topOfIndex(stackNumber)]
            self.custList[self.topOfIndex(stackNumber)] = 0
            self.sizes[stackNumber] -= 1
            return value
        
    def peek(self, stackNumber):
        if self.isEmpty(stackNumber):
            return "No item to peep."
        else:
            value = self.custList[self.topOfIndex(stackNumber)]
            return value
            
customStack = MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(3, 2)
print(customStack)
print(customStack.pop(0))
print(customStack)
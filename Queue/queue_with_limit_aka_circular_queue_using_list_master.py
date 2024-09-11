class Queue:
    def __init__(self,maxSize):
        self.items = [None] * maxSize
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top+1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self,value):
        if self.isFull():
            return "Queue is full."
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "Element has been enqueued."
        
    def dequeue(self):
        if self.isEmpty():
            return "No element to dequeue."
        else:
            removedElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = self.top = -1
            elif self.start == self.maxSize-1:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return removedElement

    def peek(self):
        if self.isEmpty():
            return "No element to peek."
        else:
            return self.items[self.start]
        
    def deleteAll(self):
        self.items = [None]*self.maxSize
        self.start = self.top = -1
         
que = Queue(4)
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
print(que.dequeue())
print(que.dequeue())
print("Peeking here:")
print(que.peek())
print("After Deque the que looks like: ")
print(que)
print("Is queue full?",que.isFull())  
print("Is queue empty?",que.isEmpty())
que.deleteAll()
print("After delete method")
print(que)
print("Is queue full?",que.isFull())  
print("Is queue empty?",que.isEmpty())

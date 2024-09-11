class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
        
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
    def enque(self,value):
        self.items.append(value)
        
    def deque(self):
        if self.isEmpty():
            return "No elements to deque"
        else:
            return self.items.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "No elemet present to peek"
        else:
            return self.items[0]
        
    def delete(self):
        self.items = []

que = Queue()
print(que.isEmpty())
que.enque(1)
que.enque(2)
que.enque(3)
print("The dequed element is:",que.deque())
print("The new que looks like:")
print(que)
print("peeked elemet:",que.peek())
que.delete()
print(que)

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return ' '.join(values)

    def enqueue(self,value):
        newNode = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "No item to deque."
        else:
            dequedElement = self.LinkedList.head
            if self.LinkedList.head.next is None:
                self.LinkedList.head = self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next

            return dequedElement
        
    def peek(self):
        if self.isEmpty():
            return "No item to deque."
        else:
            return self.LinkedList.head

    def delete(self):
        self.LinkedList.head = self.LinkedList.tail = None

q = Queue()
print("Is que empty:",q.isEmpty())
print("After enque que looks like:")
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
print("Peeking here:",q.peek())
print(q.dequeue())
print(q.dequeue())


print("After Dequeu que looks like:")
print(q)
q.delete()
print("After delete method:",q)




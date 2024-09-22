class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
#This below __str__ will print the node value if wanted.
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def __str__(self):
    
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value) 
            temp= temp.next
            if temp == self.head:
                break
            result += '->'
        return result

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

        self.length += 1

    def prepand(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        
        self.length += 1

    def insert(self,index,value):
        new_node = Node(value)
        if index > self.length or index < 0:
            raise Exception("Index out of range")
        
        if index == 0:
            if self.length == 0:
                self.head = self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head

        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

        self.length += 1

    def get(self, index):

        if index < 0 or index >= self.length:
            return None
        
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        
        return temp_node

    def set(self,index,value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None

        self.length -= 1
        return popped_node
    
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = self.tail = None
        else:
            tmp = self.head
            while tmp.next is not self.tail:
                tmp = tmp.next
                
            tmp.next = self.head
            self.tail = tmp
            popped_node.next = None
        
        self.length -= 1
        return popped_node
    
    def remove(self,index):

        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            self.pop_first()
        elif index == self.length-1:
            self.pop()
        else:
            prev_node = self.get(index-1)
            removed_node = prev_node.next
            prev_node.next = removed_node.next
            removed_node.next = None        
            self.length -= 1
            return removed_node

    def delete_all(self):

        #This if condition is for using delete_all two times.
        #If this if was not used it will RAISE AN ERROR.
        if self.length == 0:
            return
        
        self.tail.next = None
        self.head = self.tail = None
        self.length = 0
        


csLL = CSLinkedList()
csLL.append(5)
csLL.append(10)
csLL.append(17)
csLL.append(20)
csLL.prepand(2)
csLL.insert(3,15)
print("Use of get method:",csLL.get(2))
print("Length of CSLL:",csLL.length)
print("CSLL looks like:",csLL)
csLL.set(-2,43)
print("Popped first node:",csLL.pop_first())
print("Popped node:",csLL.pop())
print("Before using remove CSLL looks like:",csLL)
csLL.remove(2)
print("New CSLL looks like:",csLL)
csLL.delete_all()
print("New CSLL looks like:",csLL)
print(csLL.length)
csLL.delete_all()

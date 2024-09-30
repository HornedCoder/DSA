class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        
        return result

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepand(self,value):
        new_node = Node(value)
        if self.head is None:
             self.head = new_node
             self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1

    def insert(self,index,value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            tmp_node = self.head
            for _ in range(index-1):
                tmp_node = tmp_node.next

            new_node.next = tmp_node.next
            tmp_node.next = new_node
        self.length += 1
        return True
    
    def traverse(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return(current)   #If we do return(current.value) it will return the object value i.e node's value only.
    

    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length == 0:
            return None
        popped = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped.next = None
        self.length -= 1
        return popped
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node
    
    def remove(self,index):
        if index == 0:
            return self.pop_first()
        if index < 0 or index >= self.length:
            return None
        if index == self.length-1:
            return self.pop()
        
        previous = self.get(index-1)
        popped_node = previous.next
        previous.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.prepand(5)
new_linked_list.insert(9,15)
new_linked_list.insert(0,0)
new_linked_list.insert(3,15)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)
print(new_linked_list.length)
print(new_linked_list)
new_linked_list.traverse()
print(new_linked_list.get(2))
print(new_linked_list.set(2, 17))
print(new_linked_list)
print("Popped first element is:",new_linked_list.pop_first())
print(new_linked_list)
print("Popped last element is:",new_linked_list.pop())
print(new_linked_list)
new_linked_list.remove(2)
print(new_linked_list)
new_linked_list.delete_all()
print("Empty Linked List by delete all:",new_linked_list)
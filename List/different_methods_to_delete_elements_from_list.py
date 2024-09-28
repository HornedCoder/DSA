print("Pop Method: ")
myList = [1,2,3,4,5,6]
print("original List: ",myList)

myList.pop(2)
print("After using pop(2): ",myList)

myList.pop()
print("After using pop(): ",myList)

print("We will now use print(pop()) to see the output: ",myList.pop())    #Here it will show 5 not 6 because each time pop() is called a new element is popped.

print("We will now use print(pop(1)) to see the output: ",myList.pop(1))
print("New List: ",myList)

print("Delete method: ")
myNewList = [1,2,3,4,5,6]
print("original List: ",myNewList)
del myNewList[1]
print("After using del myNewList[1]",myNewList)

del myNewList[0:2]
print("After using del myNewList[0:2]",myNewList)

print("Remove method: ")
print("New List: ",myNewList)
myNewList.remove(5)     #This remove method takes elemet as parameter and removes that element from List.
print("After using remove(5): ",myNewList)
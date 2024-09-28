myList = [1,2,3]
print("Initila List: ",myList)

myList.insert(1,4)
print("Using Insert method, now new List: ",myList)

myList.append(11)
print("Using append method, now new List: ",myList)

newList = [11,22]
myList.extend(newList)
print("After using extend method: ",myList)
#General idea is "newList = [newItem for Item in List if Condition]"

prevList = [1,-20,35,5,-98,87,-99]
newList = [number for number in prevList if number > 0]
print("previous List: ",prevList)
print("New List: ",newList)
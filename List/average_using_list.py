myLst = list()

while True:
    inp = input("enter a number: ")
    if inp == "Done": break

    value = float(inp)
    myLst.append(inp)

    avg = sum(myLst)/len(myLst)

print("The lsit is: ",myLst)
print("Average of all elements in list is:",avg)
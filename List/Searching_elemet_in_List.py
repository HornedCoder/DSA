myList = [10,20,30,40,50,60,70,80,90]
key = 60

#Using In operator to search. It takes O(N) T.C as it does Linear search in the backend.
if key in myList:
    print(key, " is present in the List")
else:
    print(key, " is not present in the List")

#Using Linear Search now.
def Linear_Search(myList, key):
    for i in range(len(myList)):
        if key == myList[i]:
            return('Key found at index ' +str(i))
    
    return("Key Not Found.")

print(Linear_Search(myList,key))
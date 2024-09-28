import array

arr= array.array('i', [0,1,2,3,4])
print("Initial array",arr)
index=2

def delete_element(arr,index):
    
    for i in range(len(arr)):
        if i == index:
            for j in range(i, len(arr)):
                if j == len(arr)-1:
                    arr[j] = 0
                else:  
                    arr[j] = arr[j+1]

    return arr


print(delete_element(arr,index))

#The above is not very code. It is a brute force method and gives 0 in the end instead of Null.
# We can use the easy way like this:


arr= array.array('i', [0,1,2,3,4])
print("Initial array",arr)

arr.remove(3)
print("New array:",arr)

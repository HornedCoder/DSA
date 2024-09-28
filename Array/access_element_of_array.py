import array

def access_element(arr,index):

    if  index > (len(arr) -1):
        print("This index does not exist in this array")

    else:
        print(arr[index])


arr = array.array('i', [0,1,2,3])




access_element(arr,4)

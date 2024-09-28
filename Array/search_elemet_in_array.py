import array

arr = array.array('i', [0,1,2,3,8,9])
key = 9

def search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            print("The key was at index",i)
            break
        else:
            continue

    if i == (len(arr)-1):
        print('Key not found')


search(arr,key)
import math
def binarySearch(arr, value):
    start = 0
    end = len(arr)-1
    mid = math.floor((start+end)/2)

    #print(start,mid,end)
    while not(arr[mid] == value) and start <= end:
        if value < arr[mid]:
            end = mid-1
        else:
            start = mid+1
        mid = math.floor((start+end)/2)
    
    if arr[mid] == value:
        return mid
    else:
        return -1


arr = [1,2,3,4,5,6]
print(binarySearch(arr, 4))

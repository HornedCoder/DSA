arr = [3,4,1,5,2]

def maxP(arr):
    max1 = 0
    max2 = 0
    largest_no = 0
    for i in arr:
        if (i > max1):
            max2 = max1
            max1 = i
            
        elif (i > max2):
            max2 = i


    return(max1 * max2)

print(maxP(arr))

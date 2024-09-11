#Find the missing number in a list of array.

arr = [1,2,3,4,6,7,8,9,10]

def missing_no(arr,n):
    sum1 = (n*(n+1))/2
    sum2 = sum(arr)

    missing_no_is = sum1-sum2

    return(missing_no_is)

print(missing_no(arr,10))

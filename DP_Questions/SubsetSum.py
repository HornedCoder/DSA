'''
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
Example:

Input: [3, 34, 4, 12, 5, 2], sum = 9
Output: True  
There is a subset (4, 5) with sum 9.
 
Input: [3, 34, 4, 12, 5, 2], sum = 30
Output: False
There is no subset that add up to 30.
'''

def isSubsetSum(set, n, sum):
    # TODO
    if n == 0 or sum == 0:
        return False
    
    dp = [[0]* (n+1) for _ in range(n+1)]
    for i in range(n-1):
        for j in range(i+1,n):
            if set[i]+set[j] == sum:
                return True
    return False


print(isSubsetSum([3, 34, 4, 12, 5, 2],6,30))
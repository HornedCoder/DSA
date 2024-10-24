'''
Create a function to find the length of Longest Repeated Subsequence. The longest repeated subsequence (LRS) is the longest subsequence of a string that occurs at least twice.

Example

LRSLength('ATAKTKGGA',9,9) # 4 LRS = ATKG #
Note: 9 is the length of the string.
'''

#m and n are the length of the substring.
def LRS(X,m,n):
    #If either of the substring reach 0 length return
    if m == 0 or n == 0:
        return 0
    #If substrings match but their indexes doesn't match.
    if X[m-1] == X[n-1] and m!=n:
        return 1+ LRS(X,m-1,n-1)
    
    #Return else condition
    return max(LRS(X,m-1,n),LRS(X,m,n-1))

print(LRS("ATAKTKGGA",9,9))
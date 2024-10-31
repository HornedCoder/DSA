'''
Length of Longest Palindromic Subsequence
Given a sequence, find the length of the longest palindromic subsequence in it using dynamic programming.

Palindrome is a string that reads the same backward as well as forward.

Example:

lps("ABABCBA") # 5
'''

# This code 3 parameters.
def lps(S,start,end):
    # TODO
    if start > end:
        return 0
    if S[start] == S[end] and start==end:
        return 1
    if S[start] == S[end]:
        return 2+lps(S,start+1,end-1)
    else:
        return max(lps(S,start+1,end),lps(S,start,end-1))
    


print(lps("ABABCBA",0,6))

#   The following uses only one pareameter i.e. string.

def LCSLengt(S):
    n = len(S)
    l = [[0 for x in range(n) ] for x in range(n)]
    for i in range(n):
        l[i][i] = 1

    for c1 in range(2, n+1):
        for i in range(n-c1+1):
            j = c1+i-1
            if S[i] == S[j] and c1 == 2:
                l[i][j] = 2
            elif S[i] == S[j]:
                l[i][j] = l[i+1][j-1]+2
            else:
                l[i][j] = max(l[i+1][j],l[i][j-1])
        
    return l[0][n-1]

print(LCSLengt("ABABCBA"))            
            
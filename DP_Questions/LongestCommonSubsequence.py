'''
S1 and S2 are given strings, create a function to print all possible longest subsequence which is common to both strings.

Subsequence: a sequence that can be driven from another sequence by deleting some elements without changing the order of them

Example

Input:
 
S1 = "ABCBDAB"
S2 = "BDCABA"
 
Ouput:
 
"BCAB"
"BCBA"
"BDAB"

'''

def LCS(s1,s2,m,n,T):
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i-1][j],T[i][j-1])


def LCSLength(S1,S2,m,n,T):
    if m == 0 or n == 0:
        return str()
    
    if S1[m-1] == S2[n-1]:
        return LCSLength(S1,S2,m-1,n-1,T) + S1[m-1]
    
    if T[m-1][n] > T[m][n-1]:
        return LCSLength(S1,S2,m-1,n,T)
    else:
        return LCSLength(S1,S2,m,n-1,T)
    

X = "ABCBDAB"
Y = "BDCABA"
m = len(X)
n = len(Y)
 
    # T[i][j] stores the length of LCS of substring X[0..i-1], Y[0..j-1]
T = [[0 for x in range(n + 1)] for y in range(m + 1)]

LCS(X,Y,m,n,T)
print(LCSLength(X,Y,m,n,T))
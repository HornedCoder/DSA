'''
Longest Common Subsequence Length problem
S1 and S2 are given strings, create a function to find the length of the longest subsequence which is common to both strings.

Subsequence: a sequence that can be driven from another sequence by deleting some elements without changing the order of them

Example

S1 = "ABCBDAB"
S2 = "BDCABA"
 
LCSLength(S1, S2, len(S1), len(S2)) #4
'''

def LCSLength(S1, S2, lenS1, lenS2):
    # TODO
    if lenS1 == 0 or lenS2 == 0:
        return 0
    if S1[lenS1-1] == S2[lenS2-1]:
        return 1+ LCSLength(S1,S2,lenS1-1,lenS2-1)
        
    else:
        return max(LCSLength(S1,S2,lenS1-1,lenS2), LCSLength(S1,S2,lenS1,lenS2-1))
    

s1 = "ABCBDAB"
s2 = "BDCABA"
print(LCSLength(s1,s2,len(s1),len(s2)))
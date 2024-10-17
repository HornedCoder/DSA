'''
Ques:   S1 and S2 are two strings.
        Find the length of the longest
        subsequence which is common to both
        strings.
        3 letters Subsequence of 'ABCDE'
        can be 'ACE','ADE','ACB'

        S1 = 'elephant'
        S2 = 'erepat'
        O/P=> 5
        Longest String "eepat"
'''

def LCS(s1,s2,index1,index2):
    if index1 >= len(s1) or index2 >= len(s2):
        return 0
    elif s1[index1] == s2[index2]:
        return 1 + LCS(s1,s2,index1+1,index2+1)
    else:
        op1 = LCS(s1,s2,index1,index2+1)
        op2  = LCS(s1,s2,index1+1,index2)
    return max(op1,op2)

s1 = "elephant"
s2 = "erepat"

print(LCS(s1,s2,0,0))
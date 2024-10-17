'''
Ques:   S is a given string
        Find the longest palindromic subsequence.
        Example =>
            S = "ELRMENMET"
            O/P = 5
            LPS: "EMEME"
'''

def LPS(S,startIndex,endIndex):
    if startIndex > endIndex:
        return 0
    elif startIndex == endIndex:
        return 1
    elif S[startIndex] == S[endIndex]:
        return 2 + LPS(S,startIndex+1,endIndex-1)
    
    else:
        op1 = LPS(S,startIndex+1,endIndex)
        op2 = LPS(S,startIndex,endIndex-1)

        return max(op1,op2)
    
print(LPS("ELRMENMET",0,len("ELRMENMET")-1))
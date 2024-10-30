'''
The shortest common super sequence (SCS) is the problem of finding the shortest super sequence supSeq of given sequences S1 and S2 such that both these sequences are subseqeunce of supSeq.

Example

S1 = "ABCBDAB"
S2 = "BDCABA"
 
SCSLength(S1, S2, len(S1), len(S2)) #9
'''

def SCSLength(S1, S2, lenS1, lenS2):
    # TODO
    if lenS1 == 0 or lenS2 == 0:
        return lenS1+lenS2
    
    if S1[lenS1-1] == S2[lenS2-1]:
        return SCSLength(S1,S2,lenS1-1,lenS2-1)+1
    else:
        return min(SCSLength(S1,S2,lenS1-1,lenS2)+1, SCSLength(S1,S2,lenS1,lenS2-1)+1)
    

S1 = "ABCBDAB"
S2 = "BDCABA"
 
print(SCSLength(S1, S2, len(S1), len(S2)))
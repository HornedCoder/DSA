'''
    S1 and S2 are two given strings.
    Convert S2 to S1 using delete , insert or replace operations.
    Find the min. count of edit operations.
'''

def minOperation(S1,S2,index1,index2):
    if index1 == len(S1):
        return len(S2)-index2
    if index2 == len(S2):
        return len(S1) -index1
    if S1[index1] == S2[index2]:
        return minOperation(S1,S2,index1+1,index2+1)
    
    else:
        deleteOP = 1 + minOperation(S1,S2,index1,index2+1)
        insertOP = 1 + minOperation(S1,S2,index1+1,index2)
        replaceOp = 1 + minOperation(S1,S2,index1+1,index2+1)
        return(min(deleteOP,insertOP,replaceOp))

S1 = "table"
S2 = "taable"

print(minOperation(S1,S2,0,0))
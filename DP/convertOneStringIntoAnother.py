'''
Ques: S1 and S2 are two different strings.
Find out how many min operations(insert,delete and replace)
needs to convert S2 into S1.
'''

#The following is a top-down approach.
def convert(s1,s2,index1,index2,d):
    if index1 == len(s1):
        return len(s2) - index2
    elif index2 == len(s2):
        return len(s1) - index1
    elif s1[index1] == s2[index2]:
        return convert(s1,s2,index1+1,index2+1,d)
    else:
        dictKey = str(index1) + str(index2)
        if dictKey not in d:
            d[dictKey] = min((1+convert(s1,s2,index1+1,index2,d)),(1+convert(s1,s2,index1,index2+1,d)),(1+convert(s1,s2,index1+1,index2+1,d)))
                            
        return d[dictKey]

S1 = "yoru"
S2 = "ylor"
d = {}
print(convert(S1,S2,0,0,d))

#Now lets try bottom-up approach.

def convert2(s1,s2):
    tempDict = {}
    for i1 in range (len(s1)+1):
        dictKey = str(i1) + ' '+ '0'
        tempDict[dictKey] = i1
    for i2 in range(len(s2)+1):
        dictKey = '0'+ ' ' +str(i2)
        tempDict[dictKey] = i2

    for i1 in range(1,len(s1)+1):
        for i2 in range(1,len(s2)+1):
            if s1[i1-1] == s2[i2-1]:
                dictKey = str(i1)+ ' ' +str(i2)
                dictKey1 = str(i1-1)+ ' ' +str(i2-1)
                tempDict[dictKey] = tempDict[dictKey1]
            else:
                dictKey = str(i1)+ ' ' +str(i2)
                dictKeyD = str(i1-1)+ ' ' +str(i2)
                dictKeyI = str(i1)+ ' ' +str(i2-1)
                dictKeyR = str(i1-1)+ ' ' +str(i2-1)
                tempDict[dictKey] = 1 + min(tempDict[dictKeyD],tempDict[dictKeyI],tempDict[dictKeyR])


    
    dictKey = str(len(s1))+ ' ' +str(len(s2))
    return tempDict[dictKey]


L1 = 'ascws'
L2 = 'aecw'
temp = {}
print(convert2(L1,L2))

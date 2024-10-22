'''
Ques:Given N number of houses along the street
with some amount of money.
Adjacent houses can't be stolen.
Find the max amount that can be stolen
'''

#The following is top-down approach
def HR(houses, currHouse, d):
    if currHouse >= len(houses):
        return 0
    else:
        if currHouse not in d:
            d[currHouse] = max(houses[currHouse] + HR(houses, currHouse+2,d), HR(houses, currHouse+1, d))
        return d[currHouse]
    

d = {}
houses = [6,7,1,30,8,2,4]
print(HR(houses, 0, d))

#lets Try bottom-up approach.

def HR2(houses):
    lst = [0] * (len(houses) + 2)
    for i in range(len(houses)-1,-1,-1):
        lst[i] = max((houses[i]+lst[i+2]), lst[i+1])
    return lst[0]

print(HR2(houses))
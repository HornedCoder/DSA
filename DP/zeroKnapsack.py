'''
Ques:   Given the weights and profits of N items
        Find the max profit within given capacity of C.
        Items cant be broken.
'''

#This a top-down approach.

class Item:
    def __init__(self,value,weight):
        self.value = value
        self.weight = weight

def ZK(items, currItem, capacity, tempDict):
    dictKey = str(currItem) + str(capacity)
    if capacity <= 0 or currItem < 0  or currItem >= len(items):
        return 0
    elif dictKey in tempDict:
        return tempDict[dictKey]
    elif items[currItem].weight <= capacity:
        profit1 = items[currItem].value + ZK(items, currItem+1,capacity-items[currItem].weight,tempDict)
        profit2 = ZK(items,currItem+1,capacity,tempDict)
        tempDict[dictKey] = max(profit1,profit2)
        return tempDict[dictKey]
    else:
        return 0
    
Mango = Item(31,3)
Apple = Item(26,1)
Orange = Item(17,2)
Banana = Item(72,5)

items = [Mango,Apple,Orange,Banana]
print(ZK(items,0,7,{}))

#The following will be bottom-up approach.

def ZK2(profits,weights,capacity):

    if len(profits) == 0 or len(weights)!=len(profits) or capacity <= 0:
        return 0

    noOfRows = len(profits)+1
    dp = [[0 for i in range(capacity+2)] for j in range(noOfRows)]

    for i in range(noOfRows):
        dp[i][0] = 0
    for i in range(capacity+1):
        dp[noOfRows-1][i] = 0

    for row in range(noOfRows-2,-1,-1):
        for column in range(1,capacity+1):
            profit1,profit2 = 0,0
            if column >= weights[row]:
                profit1 = profits[row] + dp[row+1][column-weights[row]]
                profit2 = dp[row+1][column]
                dp[row][column] = max(profit1,profit2)
    return(dp[0][capacity]) 

profits = [ 31, 26, 72, 17 ]

weights = [ 3, 1, 5, 2 ]

capacity = 7
print(ZK2(profits,weights,capacity))
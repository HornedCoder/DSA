'''
Ques:   Given the wrights and profits
        of N items.
        Find the maximum profit within
        given capacity of C
        Items can't be broken.
'''

class Item:
    def __init__(self,value,weight):
        self.weight = weight
        self.value = value

def zeroKnap(items, capacity, currentIndex):
    if capacity <= 0 or currentIndex < 0 or currentIndex >=len(items):
        return 0
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].value + zeroKnap(items,capacity-items[currentIndex].weight,currentIndex+1)
        profit2 = zeroKnap(items,capacity,currentIndex+1)
        return max(profit1,profit2)
    else:
        return 0
    

Mango = Item(31,3)
Apple = Item(26,1)
Orange = Item(17,2)
Banana = Item(72,5)

items = [Mango,Apple,Orange,Banana]
print(zeroKnap(items,7,0))
class Item:
    def __init__(self,weight,value):
        self.value = value
        self.weight = weight
        self.ratio = value/weight

    
def Knapsack(items,capacity):
    items.sort(key = lambda x: x.ratio, reverse = True)
    usedCapacity, totalValue = 0,0

    for i in items:
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value
        else:
            unusedCapacity = capacity - usedCapacity
            value = i.ratio * unusedCapacity
            usedCapacity += unusedCapacity
            totalValue += value

        if usedCapacity == capacity:
            break

    print(totalValue)

item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)
CList = [item1,item2,item3]
Knapsack(CList,50)             
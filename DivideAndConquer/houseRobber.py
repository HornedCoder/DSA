'''
Ques:   Given N number of houses along the street with some amount of money.
        Adjacent houses can't be stolen.
        Find the max amount that can be stolen.
'''

#   houses is the list of houses with some value. currentHouse stores index of current house.
def maxHouseRobbed(houses, currentHouse):
    if currentHouse >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentHouse] + maxHouseRobbed(houses,currentHouse+2)
        skipFirstHouse = maxHouseRobbed(houses, currentHouse+1)
        return max(stealFirstHouse,skipFirstHouse)
    
houses = [6,7,1,30,8,2,4]
print(maxHouseRobbed(houses,0))


    
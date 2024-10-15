'''
    You are given coins of different denominations
    and total amount of money. Find the minimum
    number of coins that you need to make up
    the given amount.
'''

coins = [1,2,5,10,20,50,100]

#This method takes more time O(N^2)
def coinsChange(amount, coins):
    ans = []
    N = amount
    coins.sort(reverse = True)
    while N != 0:
        for i in range(len(coins)):
            if N >= coins[i]:
                N = N-coins[i]
                ans.append(coins[i])
                break
            else:
                continue
    print(ans)

#This takes O(N)
def coinsChange2(amount,coins):
    coins.sort()
    index = len(coins)-1
    while True:
        coinValue = coins[index]
        if amount >= coinValue:
            print(coinValue)
            amount = amount-coinValue
        
        if amount < coinValue:
            index -= 1
        
        if amount == 0:
            break

coinsChange(209, coins)
coinsChange2(209,coins)
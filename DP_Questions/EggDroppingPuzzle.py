'''
The following is a description of the instance of this famous puzzle involving N=2 eggs and a building with H=36 floors:

Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from, and which will cause the eggs to break on landing. We make a few assumptions:

An egg that survives a fall can be used again.

A broken egg must be discarded.

The effect of a fall is the same for all eggs.

If an egg breaks when dropped, then it would break if dropped from a higher window.

If an egg survives a fall, then it would survive a shorter fall.

It is not ruled out that the first-floor windows break eggs, nor is it ruled out that eggs can survive the 36th-floor windows.

If only one egg is available and we wish to be sure of obtaining the right result, the experiment can be carried out in only one way. Drop the egg from the first-floor window; if it survives, drop it from the second-floor window. Continue upward until it breaks. In the worst case, this method may require 36 droppings. Suppose 2 eggs are available. What is the lowest number of egg-droppings that is guaranteed to work in all cases?
'''

INT_MAX = 32767
  
# Function to get minimum number of trials needed in worst 
# case with n eggs and k floors 
def eggDrop(floors, eggs=2):
     
    dp = [[0 for _ in range(floors + 1)] for _ in range(eggs + 1)]

    #If we have only one egg, we need to drop
    #it from each floor.
    for f in range(1,floors+1):
        dp[1][f] = f

    #fill the dp table for 2 eggs.
    for e in range(2,eggs+1):
        for f in range(1,floors+1):
            #Initialise min drops as a large number
            dp[e][f] = INT_MAX
            #Check all possible floors
            for x in range(1,f+1):
                res = 1 + max(dp[e-1][x-1],dp[e][f-x])
                dp[e][f] = min(dp[e][f],res)
    
    return dp[eggs][floors]

floors = 36
print(eggDrop(floors))
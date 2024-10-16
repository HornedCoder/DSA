'''
    Ques:   Given N, find the number of ways
    to express N as sum of 1,3 and 4.
'''

def noOfFactor(N):
    if N in (0,1,2):
        return 1
    elif N == 3:
        return 2
    else:
        sub1 = noOfFactor(N-1)
        sub2 = noOfFactor(N-3)
        sub3 = noOfFactor(N-4)
    
    return sub1+sub2+sub3

print(noOfFactor(7))
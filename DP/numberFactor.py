'''
Ques:   Given a number N, find number of ways to represent it as sum of 4,3 and 1.
'''
#The following is a top-down approach
def NF(N, d):
    if N in (0,1,2):
        return 1
    if N == 3:
        return 2
    else:
        if N not in d:
            rec1 = NF(N-4,d)
            rec2 = NF(N-3,d)
            rec3 = NF(N-1,d)
            d[N] = rec1+rec2+rec3
        return d[N]
    
d = {}
print(NF(5,d))

#   Lets try bottom-up approach
def NF2(N):
    lst = [1,1,1,2]
    for i in range(4,N+1):
        lst.append(lst[i-1] +lst[i-3]+ lst[i-4])
    
    return lst[N]

print(NF2(5))
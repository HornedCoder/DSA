#This below method is memoization which is a top down approach(meaning solving from top to bottom).

def fibo(N, arr):
    if N == 1:
        return 0
    if N == 2:
        return 1

    if N not in arr:
        arr[N] = fibo(N-1, arr) + fibo(N-2, arr)

    return arr[N]


myL = {}
print(fibo(6, myL))
print(myL)


#The following is a bottom up approach called Tabulation.

def fib2(N):
    tb = [0,1]
    for i in range(2, N+1):
        tb.append(tb[i-1]+tb[i-2])
    return tb[N-1]

print(fib2(6))

     

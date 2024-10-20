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
     
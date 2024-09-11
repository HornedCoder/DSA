def fibo(n):
    if n < 0 or n != int(n):
        return "Not possible"
    if n == 1 or n == 0:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
print(fibo(7))
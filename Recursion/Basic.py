def recusrsion(n):
    if n < 1 :
        print("We got a no. less than 1")
    else:
        recusrsion(n-1)
        print(n)
        
recusrsion(4)
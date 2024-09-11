def gcd(m,n):
    ans = m %n
    if ans == 0:
        return n
    else:
        return gcd(n,ans)
    
print(gcd(21,9))
def SumOfDigs(n):
    if n < 10:
        return n
    else:
        return SumOfDigs(n//10) + n%10

print(SumOfDigs(35209))
def Power(base,exp):
    if exp == 0:
        return 1
    
    elif exp < 0:
        return 1/base * Power(base,exp+1)

    else:
        return Power(base,exp-1)*base
    
print(Power(4, -2))
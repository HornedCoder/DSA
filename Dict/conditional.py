my_dict = {'a':1,'b':2,'c':3,'d':4}

new_dict = {k:v for k,v in my_dict.items() if v%2==0}

print(new_dict)
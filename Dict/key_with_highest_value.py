my_dict = {'a':5,'b':7,'c':6}

def max_value_key(my_dict):

    return max(my_dict,key=my_dict.get)

print(max_value_key(my_dict))
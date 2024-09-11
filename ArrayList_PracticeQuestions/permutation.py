#Given two lists we have to figure if one is permutation of other.

list1 = ['m','m','o']
list2 = ['m','o','m']

def permutation(l1,l2):

    if len(l1) != len(l2):
        return False
    

    l1.sort()
    l2.sort()

    if l1 == l2:
        return True
    
    else:
        return False

print(permutation(list1,list2))


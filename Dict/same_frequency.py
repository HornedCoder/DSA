list1 = [1,2,3,2,1]
list2 = [3,1,2,1,3]

dict1 = {}
dict2 = {}

for i in list1:
    dict1[i] = dict1.get(i,0)+1

for j in list2:
    dict2[j]= dict2.get(i,0)+1

if dict1 == dict2:
    print('True')
else:
    print('False')

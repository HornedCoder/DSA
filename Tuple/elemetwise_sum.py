tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
'''
list1 = []
for i in range (len(tuple1)):
    list1.append(tuple1[i]+tuple2[i])
    
print(list1)
tuple1 = tuple(list1)
print(tuple1)
'''

tup1 = tuple(a+b for a,b in zip(tuple1,tuple2))
print(tup1)

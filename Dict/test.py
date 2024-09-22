'''
my_dict = {1:"wef",1:"dvs"}
print(my_dict)

city = ["Paris", "London"]
numbers = [1,2]

new_dict = {city[i]:numbers[i] for i in range(len(city))}
print(new_dict)

names = ["Apple","Orange"]
newDict = {}
for i in names:
    count = 0
    if i

words = ['apple','orange','banana','apple','orange','apple']

unique_words = []
for i in words:
    if i not in unique_words:
        unique_words.append(i)

print(unique_words)

frequency = []


for i in range(len(unique_words)):
    count = 0
    for j in range(len(words)):
        if unique_words[i] == words[j]:
            count+=1

    frequency.append(count)

print(frequency)

new_dict1 = {unique_words[i]:frequency[i] for i in range(len(unique_words))}
print(new_dict1)



dict2 = {'b':3,'c':4,'d':5}

new_dict = {}
for i in dict1:
    if i in dict2:
        new_dict[i] = new_dict.get(i,dict1[i])+ dict2[i]

    else:
        new_dict[i] = new_dict.get(i,dict1[i])

for j in dict2:
    if j in dict1:
        continue
    else:
        new_dict[j] = new_dict.get(j,dict2[j])

print(new_dict)

dict1 = {'a':1,'b':2,'c':3}
mac = None
mac = 'a'
print(mac)
max_value = 0
for key,value in dict1.items():
    if max_value < value:
        max_value = value

for key in dict1:
    if dict1[key] == max_value:
        print(key)
        

dict1 = {'a':1,'b':2}
new_dict = {}
for key,value in dict1.items():
    new_dict[value] = key

print(new_dict) 

my_dict = {'a':1,'b':2}

new_dict = {k:v for k,v in my_dict.items() if v%2==0}
print(new_dict)

list1 = [1,2,3,2,1]
dict1 = {}
for i in list1:
    dict1[i] = dict1.get(i,0)+1

print(dict1)

list2 = [3,1,2,1,3]
dict2 = {}
for i in list2:
    dict2[i] = dict2.get(i,0)+1

print(dict2)

#for j in dict2:
#   print(dict2.get(j))


sorted_list1 = sorted(dict1)
sorted_list2 = sorted(dict2)

for i in sorted_list1:
    if dict1.get(i) == dict2.get(i):
        continue
    else:
        print("False")

print("True")
'''

dict1 = {1:'one',2:'two'}
dict2 = {2:'two',1:'one'}

if dict1 == dict2:
    print(True)
else:
    print(False)


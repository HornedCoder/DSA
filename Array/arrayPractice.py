from array import *

#1. Create an array and traverse.

print('Step1:')
arr = array('i',[0,1,2])
print(arr)

for i in arr:
    print(i)

#2. Access individual elements through index.

print('Step2:')
print(arr[2])

#3. Append any value to array using append method.

print('Step3')
arr.append(3)   #This takes 0(1) Time Complexity and it only adds element at the end.
print(arr)

#4. Insert value in array using insert method.

print('Step4:')
arr.insert(2,4)    #Two parameters are there. 1st will be the index and the 2nd will be the element.
print(arr)

#5. Extend array using extedn method.

print('Step5:')
arr.extend([6,7])   
print(arr)
#We can use extend to add two arrays as well.
arr1 = array('i',[11,12])
arr.extend(arr1)
print(arr)

#6. Add items from list into array using fromlist() method

print('Step6:')
tmpList = [11,22,11,23]
arr.fromlist(tmpList)
print(arr1)

#7. Remove element using remove() method.

print('Step7:')
print(arr)
arr.remove(11)  #11 is in two positions so remove method will remove the first 11 it sees from start.
print(arr)

#8. Remove last array element using pop() method.

print('Step8:')
print(arr)
arr.pop()
print(arr)

#9. Fetch any element index using index method()

print('Step9:')
print(arr.index(11))

#10. Use reverse method to reverse an array.

print('Step10:')
print(arr)
arr.reverse()
print(arr)

#11. Get array buffer information througfh buffer info() method.

print('Step11:')
print(arr.buffer_info())    #This buffer_info() basically gives the starting memory location and no. of elements present in array.
#The output looks like this
#(3177915562624, 9)

#12. Check the number of occurences of an element using count() method.

print('Step12:')
print(arr.count(11))

#13. Convert array to list using tolist() method.

print('Step13:')
print(arr.tolist())

#14. Sclice elements fromn array.

print('Step14:')
print(arr)
print(arr[1:5])    #Here 1 is the starting index and 5 is the range which means it will go upto index 4. 
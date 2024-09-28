import array

arr = array.array('i',[0,1,2,3])
print(arr)

#Here in the insert method insert(4,5) 4 is the inbteger being inserterd and 5 is the position where we are inserting.
#Also we have an array of suze 4 but we are inserting at position 5 because any number greter than array size will get insertrd in
#   last position
arr.insert(7,4)
print(arr)
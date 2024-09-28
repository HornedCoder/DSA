prevList = [1,2,3]

newList = [i*2 for i in prevList]
#The above line of code is list comprehension.
#The general code is""newList = [newItem for Item in List]"

print("previou List: ",prevList)
print("New List: ",newList)

language = "Python"
lst = [letter for letter in language]
print(lst)
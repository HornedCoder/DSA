#General idea is "newList = [newItem for Item in List if Condition]"

prevList = [1,-2,35,5,-9,87,-7]
newList = [number*number for number in prevList if number < 0]
print("previous List: ",prevList)
print("New List: ",newList)


sentence = "This is an example of a sentence"

def is_consonent(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonents = [i for i in sentence if is_consonent(i)]
print(consonents)
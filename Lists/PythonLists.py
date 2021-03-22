# This are basically Mutable lists
# Declared using square braces[]
# Mutable list in which elements can be added or removed
'''
WORKING WITH PYTHON LISTS
'+' >> is the List Concatenation Operator
'*' >> is the repetition Operator
'''
list = [ 'Maths', "Physics" , 40, 50, 79 ]
tinylist = ["Computer", 96]
print (list) # Prints complete list
print (list[0]) # Prints first element of the list
print (list[1:3]) # Prints elements starting from 2nd till 3rd
print (list[2:]) # Prints elements starting from 3rd element
print(list[-1]) # Prints the last element of the list
print(list[:4]) # Prints all the elements excluding the element of the fourth index
print(list[-4:-1]) #prints from the Physics to 50 not including the [-1] index
print (tinylist * 2) # Prints list two times
print (list + tinylist) # Prints concatenated lists

list = [0, "NickBwalley"] #overriden list creates a new list
print(list)

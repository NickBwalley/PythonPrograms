# List comprehension offers a shorter syntax when you want to create a new list
# based on the values of an existing list.
# Example:
#
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#
# Without list comprehension you will have to write a for statement with a conditional test inside:
# EXAMPLE WITHOUT USING LIST COMPREHENSION
thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in thislist:
    if "a" in x:
        newlist.append(x)
print(newlist)
# USING LIST COMPREHENSION
# with list comprehension you can do that with only one line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.
newlist = [x for x in fruits if x!= "kiwi"] # accepts item that are not kiwi
print(newlist)
newlist = [x for x in range(10)] # prints value from 0-9
print(newlist)
newlist = [x.upper() for x in fruits]
print(newlist) # sets value in new list to upper case
newlist = ["hello" for x in fruits] # sets all values in new list to hello
print(newlist)
# "Return the item if it is not banana, if it is banana return orange".
newlist = [x if x!= "banana" else "orange" for x in fruits]
print(newlist)
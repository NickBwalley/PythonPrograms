# append() add an item at the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# insert() adds an item at a specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# to append elements from another list to the current list the extend() is useful
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# add iterables to the list
# The extend() method does not have to append lists,
# you can add any iterable object (tuples, sets, dictionaries etc.)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
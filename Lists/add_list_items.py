# append() add an item at the end of the list
this_list = ["apple", "banana", "cherry"]
this_list.append("orange")
print(this_list)
# insert() adds an item at a specified index
this_list = ["apple", "banana", "cherry"]
this_list.insert(1, "orange")
print(this_list)
# to append elements from another list to the current list the extend() is useful
this_list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
this_list.extend(tropical)
print(this_list)
# add iterables to the list
# The extend() method does not have to append lists,
# you can add any iterable object (tuples, sets, dictionaries etc.)
this_list = ["apple", "banana", "cherry"]
this_tuple = ("kiwi", "orange")
this_list.extend(this_tuple)
print(this_list)

# remove() removes the specified item
this_list = ["apple", "banana", "cherry"]
this_list.remove("banana")
print(this_list)
# remove specified index
# pop() removes the specified index
this_list = ["apple", "banana", "cherry"]
this_list.pop(1)
print(this_list)
# NOTE: If you don't specify the index the  pop() removes the last item from the list
this_list = ["apple", "banana", "cherry"]
this_list.pop()
print(this_list)
# del() also removes and element at a specified value
this_list = ["apple", "banana", "cherry"]
del this_list[0]
print(this_list)

this_list = ["apple", "banana", "cherry"]
del this_list # deletes the entire list
# print(this_list) # throws and error because the list does not exist
# clear() empties the list
# The list remains but has no content
this_list = ["apple", "banana", "cherry"]
this_list.clear()
print(this_list)

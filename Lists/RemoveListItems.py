# remove() removes the specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# remove specified index
# pop() removes the specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# NOTE: If you don't specify the index the  pop() removes the last item from the list
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# del() also removes and element at a specified value
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist # deletes the entire list
# print(thislist) # throws and error because the list does not exist
# clear() empties the list
# The list remains but has no content
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

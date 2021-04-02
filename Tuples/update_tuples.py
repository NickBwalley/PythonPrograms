"""
Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list,
and convert the list back into a tuple.
"""
x = ("apple", "banana", "cherry")
print(x)
print(type(x))  # tuple

y = list(x) # convert the tuple to a list
y[1] = "kiwi"   # changing the value of the index[1] to "kiwi"
x = tuple(y)  # convert back to a tuple after change has been made
print(x)

# Once a tuple is created, you cannot add items to it.
"""
this_tuple = ("apple", "banana", "cherry")
this_tuple.append("orange") # This will raise an error
print(this_tuple)
"""
# Just like the workaround for changing a tuple, you can convert it into a list, add your item(s),
# and convert it back into a tuple.
this_tuple = ("apple", "banana", "cherry")
print(this_tuple)
y = list(this_tuple)
y.append("orange")
this_tuple = tuple(y)
print(this_tuple)

"""
Remove Items
Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround 
as we used for changing and adding tuple items:

"""
this_tuple = ("apple", "banana", "cherry")
y = list(this_tuple)
y.remove("apple")
this_tuple = tuple(y)
print(this_tuple)

# Or you can delete the tuple completely:
# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) # this will raise an error because the tuple no longer exists

"""
Remove() deletes the matching element from the list whereas the del and pop removes the element present at
 specified index. Difference between pop and del is that pop returns the deleted value whereas del does not.
When you use the del() when the item is not in the list it throws an error while when you use the remove() 
even if the item is not present in the list it will not throw an error. 
"""

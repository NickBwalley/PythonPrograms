# Once a set is created, you cannot change its items, but you can add new items.
#
# To add one item to a set use the add() method.
this_set = {"apple", "banana", "cherry"}

this_set.add("orange")

print(this_set)

# Add Sets
# To add items from another set into the current set, use the update() method.
this_set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

this_set.update(tropical)

print(this_set)
"""
Definition: An iterable is any Python object capable of returning its members one at a time, 
permitting it to be iterated over in a for-loop. Familiar examples of iterables include lists, tuples,
 and strings - any such sequence can be iterated over in a for-loop.
"""
# Add Any Iterable
# The object in the update() method does not have be a set,
# it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)



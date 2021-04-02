# Remove Item

# To remove an item in a set, use the remove(), or the discard() method.

# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.remove("banana")
print(thisset)
# Note: If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
print()
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop() method to remove an item, but this method will remove the last item.
# Remember that Sets are unordered, so you will not know what item that gets removed.
#
# The return value of the pop() method is the removed item.
# remove the last item of the set using the pop() method
thisset = {"apple", "banana", "cherry"}
print(thisset)
x = thisset.pop()
print(x)
print(thisset)
print()
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
print()

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) # throws an error because the set is no longer there

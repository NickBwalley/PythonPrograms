# Removing Items
# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dict)
this_dict.pop("model")
print(this_dict)
print()
# The popitem() method removes the last inserted item
# (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.popitem()
print(thisdict)
print()
# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.
print()

# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
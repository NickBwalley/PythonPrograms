# Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
# Negative Indexing
# Negative indexing means start from the end.
#
# -1 refers to the last item, -2 refers to the second last item etc.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) # prints cherry

# using the range of indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# Note: The search will start at index 2 (included) and end at index 5 (not included).
print(thistuple[2:5])

# This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
# This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# check if item exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")



# Print the second item in the tuple:
this_tuple = ("apple", "banana", "cherry")
print(this_tuple[1])
# Negative Indexing
# Negative indexing means start from the end.
#
# -1 refers to the last item, -2 refers to the second last item etc.
this_tuple = ("apple", "banana", "cherry")
print(this_tuple[-1])   # prints cherry

# using the range of indexes
this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# Note: The search will start at index 2 (included) and end at index 5 (not included).
print(this_tuple[2:5])

# This example returns the items from the beginning to, but NOT included, "kiwi":
this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[:4])
# This example returns the items from "cherry" and to the end:
this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[2:])

# This example returns the items from index -4 (included) to index -1 (excluded)
this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[-4:-1])

# check if item exists
this_tuple = ("apple", "banana", "cherry")
if "apple" in this_tuple:
  print("Yes, 'apple' is in the fruits tuple")





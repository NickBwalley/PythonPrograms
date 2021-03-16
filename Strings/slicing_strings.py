"""
SLICING 
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
"""
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
# By leaving out the start index, the range will start at the first character:
b = "Hello, World!"
print(b[:5])  # Note: 5th index is not included and its starts from element 0
# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])
# Negative Indexing
# Get the characters:
#
# From: "o" in "World!" (position -5)
#
# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])

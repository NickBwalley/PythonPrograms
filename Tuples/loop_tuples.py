"""
Loop Through a Tuple
You can loop through the tuple items by using a for loop.
"""
# Iterate through the items and print the values:
this_tuple = ("apple", "banana", "cherry")
for x in this_tuple:
    print(x)


print()
"""
Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.
"""
for x in range(len(this_tuple)):
    print(this_tuple[x])

"""
Using a While Loop
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes.

Remember to increase the index by 1 after each iteration.
"""
print()
i = 0
while i < len(this_tuple):
    print(this_tuple[i])
    i += 1

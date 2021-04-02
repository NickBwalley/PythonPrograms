# note that tuples are immutable and once created they cannot be changed or modified
"""

Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
"""
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
"""
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuple are indexed, tuples can have items with the same value:
"""

# A tuple can allow a duplicate value
this_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(this_tuple)
# determine how many item the tuple has use the len() function
print(len(this_tuple))
print(type(this_tuple))
# To create a tuple with only one item, you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple.
this_tuple = ("apple",)
print(type(this_tuple)) # class 'tuple'

# NOT a tuple
this_tuple = ("apple")
print(type(this_tuple))  # class 'str'

# tuple item datatype
# tuple can be of any datatype
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
this_tuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
my_tuple = tuple("apple")
print(this_tuple)
print(my_tuple)  # prints each letter of the tuple since it has only one element in the tuple

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered and unindexed. No duplicate members.
    Dictionary is a collection which is unordered and changeable. No duplicate members.
When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, and, it 
could mean an increase in efficiency or security.
"""
# python dictionaries
"""
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
print(thisdict)
"""
Dictionary Items
Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
"""
print(thisdict["brand"])  # key name
"""
Ordered or Unordered?
As of Python version 3.7, dictionaries are ordered. 
In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, 
and that order will not change.

Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after 
the dictionary has been created.

Duplicates Not Allowed
Dictionaries cannot have two items with the same key:
"""
# Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
# To determine how many items a dictionary has, use the len() function:
print(len(thisdict))
# The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))  # class 'dict'

print()
# Dictionaries can be useful to store Key value pairs
monthsConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    1: "Sunday"
}

print (monthsConversion["Mar"])  # First Way to Print Values from a dictionary using the key
print(monthsConversion.get("Dec", "Key Not Found!.."))  # Second way to Print Values from a Dictionary using the get()
print(monthsConversion.get(1, "Invalid Key!"))  # Default Value if invalid key is enteredd

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered and changeable. No duplicate members.
When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.


"""
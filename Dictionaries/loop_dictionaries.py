# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
#
# When looping through a dictionary, the return value are the keys of the dictionary,
# but there are methods to return the values as well.

this_dict = {
    "car": "Lexus",
    "model": "Toyota",
    "electric": False,
    "color": "orange"
}
# Print all key names in the dictionary, one by one:
for x in this_dict:
    print(x)

print()

# Print all values in the dictionary, one by one:
for x in this_dict:
    print(this_dict[x])
print()

# You can also use the values() method to return values of a dictionary:
for x in this_dict.values():
    print(x)
print()

# You can use the keys() method to return the keys of a dictionary:4
for x in this_dict.keys():
    print(x)
print()

# Loop through both keys and values, by using the items() method:
for x in this_dict.items():
    print(x)


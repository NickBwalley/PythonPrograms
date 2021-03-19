# Change Values
# You can change the value of a specific item by referring to its key name:
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict["year"] = 2018
print(this_dict)

# The update() method will update the dictionary with the items from the given argument.
#
# The argument must be a dictionary, or an iterable object with key:value pairs.
# Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
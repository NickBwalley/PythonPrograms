# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Note: This page shows you how to use LISTS as ARRAYS, however, to work with
# arrays in Python you will have to import a library, like the NumPy library.
# Arrays are used to store multiple values in one single variable:
cars = ["Ford", "Volvo", "BMW"]
# An array is a special variable, which can hold more than one value at a time.
# Access the Elements of an Array
# You refer to an array element by referring to the index number.
print(cars[1])  # print out the element at index 1

# Modify the value of the first array item:
cars[0] = "Toyota"
print(cars)
# The Length of an Array
# Use the len() method to return the length of an array (the number of elements in an array).
print(len(cars))
# Note: The length of an array is always one more than the highest array index.
print()

# Looping Array Elements
# You can use the for in loop to loop through all the elements of an array.
for x in cars:
    print(x)

# Adding Array Elements
# You can use the append() method to add an element to an array.
cars.append("Honda")
print(cars)

# Removing Array Elements
# You can use the pop() method to remove an element from the array.
cars.pop(0)
# Note: Without specifying the index of the element you want to pop() the method will
# pop the last element of the array
print(cars)
# You can also use the remove() method to remove an element from the array.
# Delete the element that has the value "Volvo":
cars.remove("Volvo")
# Note: The list's remove() method only removes the first occurrence of the specified value.
print(cars)

"""
Array Methods

Python has a set of built-in methods that you can use on lists/arrays.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list


Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

"""
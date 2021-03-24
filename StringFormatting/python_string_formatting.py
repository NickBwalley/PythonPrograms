# To make sure a string will display as expected, we can format the result with the format() method.

# String format()
# The format() method allows you to format selected parts of a string.
#
# Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?
#
# To control such values, add placeholders (curly brackets {}) in the text,
# and run the values through the format() method:

# Example
# Add a placeholder where you want to display the price:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

print()

# You can add parameters inside the curly brackets to specify how to convert the value:
# Example
# Format the price to be displayed as a number with two decimals:
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

print()

# Syntax
# string.format(value1, value2...)

# Parameter Values
# Parameter	                Description
# value1, value2...	        Required. One or more values that should be formatted and inserted in the string.
#                           The values can be A number specifying the position of the element you want to remove.
#
#                The values are either a list of values separated by commas, a key=value list, or a combination of both.
#
                            # The values can be of any data type.


# The Placeholders
# The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
# Using different placeholder values:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)

print()

# Multiple Values
# If you want to use more values, just add more values to the format() method:
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print()

# Index Numbers
# You can use index numbers (a number inside the curly brackets {0})
# to be sure the values are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print()

# Also, if you want to refer to the same value more than once, use the index number:
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

print()


# Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname},
# but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))



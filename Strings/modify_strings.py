# str to UPPERCASE()
a = "Hello, World!"
print(a.upper())
# str to LOWERCASE()
a = "Hello, World!"
print(a.lower())
print()
# REMOVE WHITE SPACES
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!
# REPLACE STRING
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
# SPLIT STRING
# The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
# STRING CONCATENATIONS
a = "Hello"
b = "World"
c = a + " " + b
print(c)

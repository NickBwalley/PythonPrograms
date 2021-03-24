'''
Modules are basically any external files that you want to use and instead of copying the content
into your page you just add the import of that external keyword inside your workspace
Pip -> You can use Pip to install external python modules(PACKAGE MANAGER)

'''

import useful_tools
import useful_tools as ut # using the alias name "ut" as a shortform

print(useful_tools.my_name("NickBwalley"))
print(useful_tools.feet_to_centimeters)
print(useful_tools.print_vowels("Nick"))

"""
Re-naming a Module
You can create an alias when you import a module, by using the as keyword:
"""
# Create an alias for useful_tools called ut:

print(ut.my_name("Serena"))

"""
Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.
"""

# Import and use the platform module:
import platform

x = platform.system()
print(x)

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
# List all the defined names belonging to the platform module:
x = dir(platform)
print(x)
# Note: The dir() function can be used on all modules, also the ones you create yourself.


# Import From Module
# You can choose to import only parts from a module, by using the from keyword.
# The module named my_module has one function and one dictionary:
def greeting(name):
    print("Hello, " + name)


person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# Import only the person1 dictionary from the module:
from my_module import person1
print(person1["age"])

# Note: When importing using the from keyword, do not use the module name when referring to elements in the module.
# Example: person1["age"], not my_module.person1["age"]


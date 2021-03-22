"""
PYTHON FUNCTIONS
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
"""


# Creating a Function
# In Python a function is defined using the def keyword:

def my_function():
    print("Hello from a function")


# Calling a Function
# To call a function, use the function name followed by parenthesis:
my_function()
print()


# Arguments
# Information can be passed into functions as arguments.
#
# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.
#
# The following example has a function with one argument (fname). When the function is
# called, we pass along a first name, which is used inside the function to print the full name:
# Arguments are often shortened to args in Python documentations.
def my_function(fname):
    print("Your name is: " + fname)


my_function("Emil")
my_function("Tobias")
my_function("Linus")
print()

"""
Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that 
are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.

Parameter is variable in the declaration of function. 
Argument is the actual value of this variable that gets passed to function.

"""


# Number of Arguments
# By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments, you have to call the function with
# 2 arguments, not more, and not less.
def your_name(f_name, l_name):
    print("Your name is: " + f_name + " " + l_name)


your_name("Nick", "Bwalley")

# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that
# if your function expects 2 arguments, you have to call the function with 2 arguments, not more,
# and not less.
print()
"""
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
"""


# Arbitrary Arguments are often shortened to *args in Python documentations.
# If the number of arguments is unknown, add a * before the parameter name:
def my_kids(*kids):
    print("The Youngest Kid is: " + kids[2])


my_kids("Jayden", "Smith", "Nicole", "Diana")

print()
"""
Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.
"""


# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
def my_kids(child3, child2, child1):
    print("The Youngest Kid is: " + child1)


my_kids(child1="Aliyah", child2="Aaron", child3="Stacy")
print()
"""
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""


# Arbitrary Keyword Arguments are often shortened to **kwargs in Python documentations.
def my_kids(**kids):
    print("His last name is: " + kids["l_name"])


my_kids(fname="Aaron", l_name="Smith")
print()
"""
Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:
"""


def my_country(country="Norway"):
    print("I am from " + country)


my_country("Sweden")
my_country("India")
my_country()
my_country("Brazil")

print()
"""
Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), 
and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:
"""


def fruit_stuffs(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
fruit_stuffs(fruits)
print()

"""
Return Values
To let a function return a value, use the return statement:
"""


def multiply_by_itself(x):
    return x * x


print(multiply_by_itself(3))  # multiplies by itself


# function to find the cube of a number
def find_cube(number):
    result = number*number*number
    return result


print(find_cube(9))

print()
"""
The pass Statement
function definitions cannot be empty, but if you for 
some reason have a function definition with no content, put in the pass statement to 
avoid getting an error.
"""


def my_function():
    pass


print()


"""
Recursion
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. 
It means that a function calls itself. This has the benefit of meaning that you can loop through 
data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a 
function which never terminates, or one that uses excess amounts of memory or processor power. 
However, when written correctly recursion can be a very efficient and mathematically-elegant 
approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). 
We use the k variable as the data, which decrements (-1) every time we recurse. 
The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, 
best way to find out is by testing and modifying it.
"""


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)  # 6+5+4+3+2+1

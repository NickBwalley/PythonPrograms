from math import *  # library to  use a lot more of math functions to use to print out values
import random
'''
PYTHON NUMBERS
There are three numeric types in Python:

int
float
complex
'''
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
print()
# int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
print()
# FLOAT
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# Float can also be scientific numbers with an "e" to indicate the power of 10
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
print()
# COMPLEX
# Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
print("---------------------------")
'''
TYPE CONVERSION
You can convert from one type to another with the int(), float(), and complex() methods:
'''
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
# Note: You cannot convert complex numbers into another number type.
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
print("------------------------------")
'''
RANDOM NUMBER
Python does not have a random() function to make a random number, 
but Python has a built-in module called   random that can be used to make random numbers:
'''

print(random.randrange(1, 10))
print("--------------------------")
print(99.99)  # basic print statement
print(79 + 99)  # basic Arithmetic Operation
print(4 - 9)  # arithmetic Operation
print(14 * 14)  # Arithmetic Operation
print(14 * (2 + 9))  # using parenthesis to specify the order of operation
print(10 % 4)  # using the modulus to get the remainder
my_num = 79  # using a variable to print out a value
print(my_num)  # prints out my_num
# for you to be able to print the number with the string you must first convert the number to string first
# then print it out else it will return an error
print(str(my_num) + " is my Favorite Number")
bronze = -9
print(abs(bronze))  # prints the absolute value of the number
print(pow(9, 2))  # the same as 9^2//returns 81
print(max(9.98, 9.99))  # prints out the maximum of the two numbers
print(min(9.98, 9.99))  # prints out the minimum of the two numbers
print(round(3.6))  # rounds off
print(floor(5.9))  # rounds down a Number
print(ceil(5.1))  # rounds up a number
print(sqrt(81.79))  # prints out the square root of a number
print(1 + 2 + 3 * (1 + 2 + 3))  # print


def get_cube_root(num):
    return num ** (1. / 3)


print(get_cube_root(num=64))  # prints out the cubeRoot of a number

'''Python is a dynamically typed language;
 hence we do not need to define the type of the variable while declaring it.
 The interpreter implicitly binds the value with its type. '''
a=10
b="Hi Python"
c = 10.5
print(type(a))
print(type(b))
print(type(c))
print("---------------------------------------------")
a = 5
print("The type of a", type(a))

b = 40.5
print("The type of b", type(b))

c = 1 + 3j
print("The type of c", type(c))
print(" c is a complex number", isinstance(1 + 3j, complex))

# In the case of string handling, the operator +
# is used to concatenate two strings as the operation "hello"+" python" returns "hello python".
# The operator * is known as a repetition operator as the operation "Python" *2 returns 'Python Python'.

str = "string using double quotes"
print(str)
s = '''A multiline
string'''
print(s)

n = '''nickbwalley'''
print(n)

print("-----------------------------------------")
# STRINGS
str1 = 'hello javatpoint' # string str1
str2 = ' how are you' # string str2
print(str1[0:2]) # printing first two character using slice operator
print(str1[4]) # printing 4th character of the string
print(str1*2) # printing the string twice
print(str1 + str2) # printing the concatenation of str1 and str2

print("-----------------------------------------")

# LISTS
# We can use slice [:] operators to access the data of the list.
# The concatenation operator (+) and repetition operator (*) works with the list in the same way as they
# were working with the strings.
list1 = [1, "hi", "Python", 2]
# Checking type of given list
print(type(list1))

# Printing the list1
print(list1)

# List slicing
print(list1[3:])

# List slicing
print(list1[0:2])

# List Concatenation using + operator
print(list1 + list1)

# List repetation using * operator
print(list1 * 3)

print("-----------------------------------------")
# TUPLE
# A tuple is a read-only data structure as we can't modify the size and value of the items of a tuple.
tup = ("hi", "Python", 2)
# Checking type of tup
print(type(tup))

# Printing the tuple
print(tup)

# Tuple slicing
print(tup[1:])
print(tup[0:1])

# Tuple concatenation using + operator
print(tup + tup)

# Tuple repatation using * operator
print(tup * 3)

# Adding value to tup. It will throw an error.
# t[2] = "hi"

print("-----------------------------------------")
# DICTIONARY
# Dictionary is an unordered set of a key-value pair of items.
# It is like an associative array or a hash table where each key stores a specific value.
# Key can hold any primitive data type, whereas value is an arbitrary Python object.
#
# The items in the dictionary are separated with the comma (,) and enclosed in the curly braces {}.
d = {
    1: 'Jimmy',
    2: 'Alex',
    3: 'john',
    4: 'mike'
}

# Printing dictionary
print(d)

# Accesing value using keys
print("1st name is " + d[1])
print("2nd name is " + d[4])

print(d.keys())
print(d.values())

print("-----------------------------------------")
# Boolean
# Boolean type provides two built-in values, True and False. These values are used to determine the given
# statement true or false. It denotes by the class bool.
# True can be represented by any non-zero value or 'T' whereas false can be represented by the 0 or 'F'.
# Consider the following example.
# Python program to check the boolean type
print(type(True))
print(type(False))

print("-----------------------------------------")
# Python Set is the unordered collection of the data type. It is iterable,
# mutable(can modify after creation), and has unique elements. In set, the order of
# the elements is undefined; it may return the changed sequence of the element.
# The set is created by using a built-in function set(), or a sequence of
# elements is passed in the curly braces and separated by the comma.
# It can contain various types of values. Consider the following example.

# Creating Empty set
set1 = set()

set2 = {'James', 2, 3, 'Python'}

# Printing Set value
print(set2)

# Adding element to the set

set2.add(10)
print(set2)

# Removing element from the set
set2.remove(2)
print(set2)

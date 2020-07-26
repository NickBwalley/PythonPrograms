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
t[2] = "hi"

print("-----------------------------------------")

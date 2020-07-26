'''Python is a dynamically typed language;
 hence we do not need to define the type of the variable while declaring it.
 The interpreter implicitly binds the value with its type. '''
a=10
b="Hi Python"
c = 10.5
print(type(a))
print(type(b))
print(type(c))
print("----------------------")
a = 5
print("The type of a", type(a))

b = 40.5
print("The type of b", type(b))

c = 1 + 3j
print("The type of c", type(c))
print(" c is a complex number", isinstance(1 + 3j, complex))  
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Note: Make sure the number of variables matches the number of values, or else you will get an error.
print("-------------")
# ONE VALUE TO MULTIPLE VARIABLES:
x = y = z = "Orange"
print(x)
print(y)
print(z)
print("-----------------")
'''
UNPACKING A COLLECTION
If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.
'''
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)
# When you run a condition in an if statement, Python returns True or False:
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))
# Evaluate two variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Almost any value is evaluated to True if it has some sort of content.
#
# Any string is True, except empty strings.
#
# Any number is True, except 0.
#
# Any list, tuple, set, and dictionary are True, except empty ones.
print(bool(0))
list1 = []
print(bool(list1))
string = ""
print(bool(string))
# In fact, there are not many values that evaluate to False, except empty values,
# such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
print("------")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print("----------")
# One more value, or object in this case, evaluates to False, and that is if
# you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0


my_obj = myclass()
print(bool(my_obj))
# function returns boolean
def my_function():
    return True


print(my_function())
# You can execute code based on the Boolean answer of a function:
def my_function2():
    return True


if my_function2():
    print("YES!")
else:
    print("NO!")


# Python also has many built-in functions that return a boolean value,
# like the isinstance() function, which can be used to determine
# if an object is of a certain data type:
x = 200
print(isinstance(x, int))  # returns boolean
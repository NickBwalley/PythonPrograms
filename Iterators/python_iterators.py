"""
Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist
of the methods __iter__() and __next__().
"""

"""
Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an 
iterator from.

All these objects have a iter() method which is used to get an iterator:
"""
# Return an iterator from a tuple, and print each value:
my_tuple = ("apple", "banana", "cherry")
my_iterator = iter(my_tuple)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

print()
# Even strings are iterable objects, and can return an iterator:
my_string = "apple"
print(len(my_string)) # check the length of the String before iterating the string
my_iterator = iter(my_string)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

print()

# Looping Through an Iterator
# We can also use a for loop to iterate through an iterable object:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

# Iterate the characters of a string:
# The for loop actually creates an iterator object and executes the next() method for each loop.
my_string = "banana"
for x in my_string:
    print(x)

print()
"""
Create an Iterator
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), 
which allows you to do some initializing when the object is being created.

The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the 
iterator object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence.
"""

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


my_class = MyNumber()
my_iter = iter(my_class)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print()

"""
StopIteration
The example above would continue forever if you had enough next() statements, or if it was used in a for loop.

To prevent the iteration to go on forever, we can use the StopIteration statement.

In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified
 number of times:
"""


# Stop after 20 iterations:
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


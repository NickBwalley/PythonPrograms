"""
Python For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary,
a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator
method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# The for loop does not require an indexing variable to set beforehand.

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:
for x in "banana":
    print(x)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
for x in fruits:
    print(x)
    if x == "banana":  # prints apple and banana then breaks and does not print the last element
        break
print()

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)  # prints only "apple" then breaks
print()

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
# Do not print banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and ends at a specified number.
for x in range(6):
    print(x) # Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
print()

# The range() function defaults to 0 as a starting value, however it is possible to
# specify the starting value by adding a parameter: range(2, 6),
# which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
    print(x)
print()

# The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
    print(x)
print()

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
    print(x)
else:
    print("Finally finished!")
# Note: The else block will NOT be executed if the loop is stopped by a break statement.
print()


# Example
# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!") # not printed out
print()


# Nested Loops
# A nested loop is a loop inside a loop.
#
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
    pass



print("------------------")
for letters in "Prickler Scurry":
    print(letters)  # prints each letter individually
friends = ["Scurry", "Dray", "Duzzler", "Prickler"]
for friend in friends:
    print(friend)   # prints out the elements in the array

for index in range(10): # prints out the values from 1 >> 10
    print(index)
print("----------")
for index in range(3, 10):
    print(index)
print("------------")
names = ["Allan", "Smith", "Peter", "Drury"]
for index in range(len(names)):
    print(names[index])
print("------------")
for item in range(7):
    if item == 0:
        print("First Iteration")
    elif item == 3:
        print("Mid Iteration")
    else:
        print(item)
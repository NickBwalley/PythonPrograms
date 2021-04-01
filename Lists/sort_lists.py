# List objects have a sort() method that will sort the list alphanumerically,
# ascending, by default:
this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort()
print(this_list)
# sort the list numerically
this_list = [100, 50, 65, 82, 23]
this_list.sort()
print(this_list)
# sort in descending order
this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort(reverse = True)
print(this_list)
# sort numbers in descending order
this_list = [100, 50, 65, 82, 23]
this_list.sort(reverse = True)
print(this_list)
# customize sort function
# You can also customize your own function by using the keyword argument key = function.
#
# The function will return a number that will be used to sort the list (the lowest number first):
# Sort the list based on how close the number is to 50:
print("-------------")


def my_function(n):
    return abs(n -50)


this_list = [100, 50, 65, 82, 23]
this_list.sort(key = my_function)
print(this_list)
print("-------------")
# case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower
# case letters:
this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.sort()
print(this_list)
# Luckily we can use built-in functions as key functions when sorting a list.
#
# So if you want a case-insensitive sort function, use str.lower as a key function:
this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.sort(key = str.lower)
print(this_list)
# reverse order
# What if you want to reverse the order of a list, regardless of the alphabet?
#
# The reverse() method reverses the current sorting order of the elements.
this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.reverse()
print(this_list)






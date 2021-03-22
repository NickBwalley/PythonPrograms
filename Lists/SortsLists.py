# List objects have a sort() method that will sort the list alphanumerically,
# ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# sort the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# sort in descending order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
# sort numbers in descending order
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
# customize sort function
# You can also customize your own function by using the keyword argument key = function.
#
# The function will return a number that will be used to sort the list (the lowest number first):
# Sort the list based on how close the number is to 50:
print("-------------")
def myFunc(n):
    return abs(n -50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myFunc)
print(thislist)
# case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower
# case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# Luckily we can use built-in functions as key functions when sorting a list.
#
# So if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
# reverse order
# What if you want to reverse the order of a list, regardless of the alphabet?
#
# The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)






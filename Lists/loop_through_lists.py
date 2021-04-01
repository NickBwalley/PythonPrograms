# print all the items in the list one by one
this_list = ["apple", "banana", "cherry"]
for x in this_list:
    print(x)
print("--------------")
# loop through the index numbers
this_list = ["apple", "banana", "cherry"]
for i in range(len(this_list)):
    print(this_list[i])
print("--------------")
# using while loop
this_list = ["apple", "banana", "cherry"]
i = 0
while i < len(this_list):
    print(this_list[i])
    i += 1
print("--------------")
# looping using list comprehension
# list comprehension offers the shortest syntax of looping through lists
# a short hand for loop that will print all the items in a list
this_list = ["apples", "banana", "cherry"]
[print(x) for x in this_list]

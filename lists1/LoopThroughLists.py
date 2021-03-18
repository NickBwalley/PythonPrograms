# print all the items in the list one by one
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
print("--------------")
# loop through the index numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
print("--------------")
# using while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i+=1
print("--------------")
# looping using list comprehension
# list comprehension offers the shortest syntax of looping through lists
# a short hand for loop that will print all the items in a list
thislist = ["apples", "banana", "cherry"]
[print(x) for x in thislist]

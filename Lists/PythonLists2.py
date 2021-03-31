
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist) # original list
thislist[1] = ["blackcurrant"] # change item value
print(thislist)
thislist[1:3] = ["Lemon", "Watermelon"] # change range of item values
print(thislist)
thislist[1:2] = ["pears", "brocolli"] # change the [1] index element  with the second value
print(thislist)
print("------------------")
# creating a new list
list2 = ["apple", "banana"]
list2.insert(1, "orange") # insert an element at index 1
print(list2)
list2.append("mango") # adds the element at the end of the list
# Note: Append adds to the end of the list, while insert adds in front of specified index
print(list2)
list2.insert(2, "tomatoes")
print(list2) # adds the element at the second index
list3 = [20, 30, 40, 50]
list2.extend(list3) # extend() method merges two lists as one
print (list2)
# remove elements from a list
list2.remove(list2[0])
list2.remove("orange")
print(list2)
# remove  specified index
# pop()
list2.pop(0) # NOTE: If you don't specify the index the pop() removes the last item
print(list2)
# delete element in a list
del thislist[0]
print(thislist)
# del() -> can also delete the list completely

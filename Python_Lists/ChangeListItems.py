thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" # replaces the element of the 1st index with "blackcurrant"
print(thislist)
# change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["Lemon", "watermelon"] # replaces the first and second index values
print(thislist)
# change the second value by replacing it with two new values
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] # replaces two values in index 1
print(thislist)
# change the second the third value by replacing with one value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] # replaces the first index value with "watermelon"
print(thislist)
# insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # insert method inserts and item at a specified index
print(thislist)
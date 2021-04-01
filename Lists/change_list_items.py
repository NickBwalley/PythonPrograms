this_list = ["apple", "banana", "cherry"]
this_list[1] = "blackcurrant"    # replaces the element of the 1st index with "blackcurrant"
print(this_list)
# change a range of item values
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
this_list[1:3] = ["Lemon", "watermelon"]    # replaces the first and second index values
print(this_list)
# change the second value by replacing it with two new values
this_list = ["apple", "banana", "cherry"]
this_list[1:2] = ["blackcurrant", "watermelon"]  # replaces two values in index 1
print(this_list)
# change the second the third value by replacing with one value
this_list = ["apple", "banana", "cherry"]
this_list[1:3] = ["watermelon"]     # replaces the first index value with "watermelon"
print(this_list)
# insert items
this_list = ["apple", "banana", "cherry"]
this_list.insert(2, "watermelon")   # insert method inserts and item at a specified index
print(this_list)

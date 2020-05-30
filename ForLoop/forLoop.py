
for letters in "Prickler Scurry":
    print(letters)#prints each letter individually
friends = ["Scurry", "Dray", "Duzzler", "Prickler"]
for friend in friends:
    print(friend)#prints out the elements in the array

for index in range(10):#prints out the values from 1 >> 10
    print(index)
print("----------")
for index in range(3,10):
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
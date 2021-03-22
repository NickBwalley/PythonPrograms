#creating a 2D list
number_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
#Accessing the elements inside the list
print(number_list[0][0])#prints out 1
print(number_list[0][1])#prints out 2
print(number_list[0][2])#prints out 2
print(number_list[1][1])#prints out 5
print(number_list[3][0])#prints out 0
#Using a NestedLoop to print the elements in the 2DList
for rows in number_list:
    print(rows)#prints out all the values inside the number_list
#printing out the values of the list individually
for rows in number_list:
    for index in rows:
        print(index)#prints out the elements individually
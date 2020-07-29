# For Loop
name = "Nick"
for str in name:
    print(str)
print("**********")
# program to print the multiplication table of 5
list = [1,2,3,4,5,6,7,8,9,10]
n = 5
for i in list:
    c = n*i
    print(c)
print("**********")
# Program to sum numbers in a list using a for loop
list2 = [5,10,15,20,25,30]
sum = 0
for j in list2:
    sum +=j
    print(sum)
print("**********")
# FOR LOOP TO PRINT(start,stop,step size)
number = int(input("Enter a Number: "))
for x in range(1,11):
    y = number * x
    print(number, "*",x, " = ", y)
print("**********")
# NESTED FOR-LOOPS
# User input for number of rows
rows = int(input("Enter the rows:"))
# Outer loop will print number of rows
for i in range(0,rows+1):
# Inner loop will print number of Astrisk
    for j in range(i):
        print("*",end = '')
    print()
print("-------BreakStatement-------")
# Using else statement with a for-Loop
for i in range(0,5):
    print(i)
else:
    print("End of the Print Statement")
print("------------------------------------")

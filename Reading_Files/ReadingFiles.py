'''
r -> read
w -> write
a -> append
r+ -> read and Write
'''

employee_file = open("index.txt", "r")
print(employee_file.readable())#returns a boolean
print("-----------------------")
#print(employee_file.read())#reads out the entire file
print("-----------------------")
print(employee_file.readline())#reads out one line
print(employee_file.readline())#reads out the next line
print("-----------------------")
print(employee_file.readlines())#takes all the lines and puts them inside an array

employee_file.close()
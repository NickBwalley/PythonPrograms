'''
r -> read
w -> write
a -> append
r+ -> read and Write
'''

employee_file = open("index.txt", "r")
print(employee_file.readable())#returns a boolean
print(employee_file.read())#prints all the values inside of the index.txt file
employee_file.close()

employee_file = open("index.txt", "r")
for employees in employee_file.readlines():
    print(employees)
employee_file.close()
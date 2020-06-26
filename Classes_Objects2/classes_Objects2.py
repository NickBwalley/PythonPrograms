class Employees:
    pass

emp_1 = Employees()
emp_2 = Employees()

print(emp_1)
emp_1.first = 'Nicholas'
emp_1.second = 'Bwalley'
emp_1.email = 'Nicholas.Bwalley@strathmore.edu'
emp_1.pay = 50000

emp_2.first = 'Elly'
emp_2.second = 'Goulding'
emp_2.email = 'Elly.Goulding@strathmore.edu'
emp_2.pay = 40000

print(emp_1.first)
print(emp_2.email)
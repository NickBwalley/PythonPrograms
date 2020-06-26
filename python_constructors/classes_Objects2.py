class Employees:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@strathmore.edu'
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employees("Nicholas", "Bwalley", 50000)
emp_2 = Employees("Elly", "Goulding", 45000)

print(emp_1.email)
print(emp_2.email)
print("---------------")
print(emp_1.fullname()) # This is an instance so the instance is going to be passed automatically
print(emp_2.fullname())
print("---------------")
print(Employees.fullname(emp_1)) # This we are calling the class and invoking the instance manually

# print(emp_1)
# emp_1.first = 'Nicholas'
# emp_1.second = 'Bwalley'
# emp_1.email = 'Nicholas.Bwalley@strathmore.edu'
# emp_1.pay = 50000
#
# emp_2.first = 'Elly'
# emp_2.second = 'Goulding'
# emp_2.email = 'Elly.Goulding@strathmore.edu'
# emp_2.pay = 40000
#
# print(emp_1.first)
# print(emp_2.email)
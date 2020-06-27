# PYTHON CONSTRUCTORS
'''
A constructor is a special type of method (function)
which is used to initialize the instance members of the class.
In C++ or Java, the constructor has the same name as its class,
but it treats constructor differently in Python. It is used to create an object.
'''
class Students:
    def __init__(self, name, std_no, course):
        self.name = name
        self.std_no = std_no
        self.course = course
    def student_details_1(self):
        return '{} {} {}'.format(self.name, self.std_no, self.course)

std_1 = Students("Nicholas Bwalley", 122790, "DBIT")
std_2 = Students("Lorna Karuma", 122994, "DBIT")
std_3 = Students("Ivy Felicia", 120990, "DBIT")

print(Students.student_details_1(std_1))# Invoking the class and passing the object as the parameter
print(std_1.student_details_1()) # calling the method only and it passes itself inside the function



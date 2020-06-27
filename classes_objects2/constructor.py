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
print("***********************")
# PYTHON COUNTING THE NUMBER OF OBJECTS IN A CLASS
class object_numbers:
    count = 0
    def __init__(self):
        object_numbers.count += 1

obj_1  = object_numbers()
obj_2 = object_numbers()
obj_3 = object_numbers()
obj_4 = object_numbers()
print("Number of Objects are: %d"%object_numbers.count)
print("***********************")

# PYTHON PARAMETERISED CONSTRUCTOR
'''
The parameterized constructor has multiple parameters along with the self.
Consider the following example.
'''
class Animal:
    def __init__(self,name):
        print("This is  a Parameterised Constructor!")
        self.name = name

    def cat_family(self):
        print ("Hello",self.name)

animal = Animal("Tiger")
animal.cat_family()

print("***********************")

# PYTHON NON-PARAMETERISED CONSTRUCTOR
'''
The non-parameterized constructor uses when we do not want to 
manipulate the value or the constructor that has only self as an argument.
'''
class Animal:
    def __int__(self):
        print("This is a Non-parameterised Constructor")
    def dog_family(self,name):
        print("Hello ", name)
dog = Animal()
dog.dog_family("African wild Dog")


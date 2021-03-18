'''
PYTHON BUILT-IN CLASS FUNCTIONS
The built-in functions defined in the class are described in the following table.

SN	Function	Description
1	getattr(obj,name,default)	It is used to access the attribute of the object.
2	setattr(obj, name,value)	It is used to set a particular value to the specific attribute of an object.
3	delattr(obj, name)	It is used to delete a specific attribute.
4	hasattr(obj, name)	It returns true if the object contains some specific attribute.
'''

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

# creating the object of the Student class
student_one = Student("Nicholas", 20, 'B')

# printing the attribute of the name of the student_one object
print(getattr(student_one, 'name')) # Nicholas

# reset the value of attribute age to 23
setattr(student_one, "age", 23)
print(getattr(student_one, 'age'))

# boolean to check if the student contains attribute with name id
print(hasattr(student_one, 'name')) # returns true because the name attributes is there

# deletes the attribute age
delattr(student_one, 'age')
# print(student_one.age) # returns an  error

# printing all the values of the class constructor
print('{}, {}'.format(student_one.name, student_one.grades))

'''
Built-in class attributes
Along with the other attributes, a Python class also contains some built-in class attributes which provide information about the class.

The built-in class attributes are given in the below table.

SN	Attribute	Description
1	__dict__	It provides the dictionary containing the information about the class namespace.
2	__doc__	It contains a string which has the class documentation
3	__name__	It is used to access the class name.
4	__module__	It is used to access the module in which, this class is defined.
5	__bases__	It contains a tuple including all base classes.
'''


class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def student_details(self):
        print("Name %s, Age %s, Gender %s", self.name, self.age, self.gender)


st_1 = Student("Nicholas", 20, "Male")
print(st_1.__doc__)
print(st_1.__dict__)
print(st_1.__module__)
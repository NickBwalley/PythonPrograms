class student:
    student_name = "Nicholas"
    student_age = 20
    student_gender = "Male"

    def student_details(self):
        print("Name: %s, Age: %s, Gender: %s "%(self.student_name, self.student_age, self.student_gender))

# SYNTAX
# <object-name> = <class-name>(<arguments>).
std_1 = student()
std_1.student_details()

# delete the property of object
del student.student_name;

# deleting the object itself
del std_1

# print(std_1.student_details())

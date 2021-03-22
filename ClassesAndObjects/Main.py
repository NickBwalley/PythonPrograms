from MyStudent import Student
from MyDriver import BestDriver
Student1 = Student("Nicholas", 122790, 6.1, False)
Student2 = Student("Lorna", 122994, 6.0, False)
print(Student1.name)  # an object of the students class
print(Student1.stdNo)
print(Student1.gpa)
print(Student1.is_on_probation)
print("--------------")
print(Student2.name)  # different object of the Student class
print("--------------")
Number1 = BestDriver("Lewis Hamilton", 30, "Mercedes")
print(Number1.name)
print(Number1.age)
print(Number1.car_brand)
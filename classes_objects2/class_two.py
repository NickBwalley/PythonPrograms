from class_one import student

student_one = student()
student_two = student()

st_1 = student_one.student_details("Allan Smith", 19)
st_2 = student_two.student_details("Nick Biiy", 20)
print(st_1)
print(student_one) # prints the memory address of the student_one object
print("--------------")
print(st_2)
class student:
    def __init__(self):
        print("You are in Class 1..")
    def student_details(self, name, age):
        self.name = name
        self.age = age
        return 'Name: {}  Age: {} '.format(self.name, self.age)

st = student()
print(st.student_details("Martin, Carlos", 14))

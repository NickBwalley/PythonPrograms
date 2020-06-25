class student:
    def __init__(self, first, last, email, std_no):
        self.first = first;
        self.last = last;
        self.email = first + '.' + last + '@strathmore.edu'
        self.std_no = std_no

student_1 = student()
student_2 = student()

print (student_1)
print (student_2)

#first_method
student_1.first = ('Nicholas')
student_1.last = ('Bwalley')
student_1.email = ('Nicholas.Bwalley@strathmore.edu')
student_1.std_no = (122790)

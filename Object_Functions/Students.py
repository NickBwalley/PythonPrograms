class Student:
    def __init__(self, name, stdNo, course, gpa):
        self.name = name
        self.stdNo = stdNo
        self.course = course
        self.gpa = gpa

    def on_honor_roll (self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
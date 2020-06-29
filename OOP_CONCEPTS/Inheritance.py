'''
Syntax
class derive-class(<base class 1>, <base class 2>, ..... <base class n>):
    <class - suite>
'''
class Animal:
    def animal_sound(self):
        print("An Animal has no Sounds!..")

class Dog(Animal):
    def dog_sound(self):
        print("A Dog barks!..")

dog = Dog()
dog.dog_sound()
dog.animal_sound()
'''
Syntax
class derive-class(<base class 1>, <base class 2>, ..... <base class n>):
    <class - suite>
'''
# PYTHON INHERITANCE
class Animal:
    def animal_sound(self):
        print("An Animal has no Sounds!..")

class Dog(Animal):
    def dog_sound(self):
        print("A Dog barks!..")

dog = Dog()
dog.dog_sound()
dog.animal_sound()
print("*******************************")
# PYTHON MULTI-LEVEL INHERITANCE
class Animal_one:
    def animal_sound(self):
        print("An Animal has no Sound!..")

class Tiger(Animal_one):
    def tiger_sound(self):
        print("A Tiger roars and the biggest in the cat family!..")

class Cat(Tiger):
    def cat_sound(self):
        print("A Cat Meows and is the Smallest in the cat family!..")

cat_one = Cat()
cat_one.cat_sound()
cat_one.tiger_sound()
cat_one.animal_sound()
print("*******************************")
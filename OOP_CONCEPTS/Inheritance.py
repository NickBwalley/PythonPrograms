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

# PYTHON MULTIPLE INHERITANCE
class calculation1:
    def summation(self, a,b):
        return a+b
class calculation2:
    def multiplication(self, a,b):
        return a*b
class calculation3:
    def subraction(self, a,b):
        return a-b
class derived(calculation1, calculation2, calculation3):
    def division(self, a,b):
        return a/b

d = derived()
print(d.summation(10,20))
print(d.subraction(20,10))
print(d.multiplication(10,20))
print(d.division(20,10))
print("*******************************")
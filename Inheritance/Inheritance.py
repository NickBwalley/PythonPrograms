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

class animal_one:
    def animal_sound(self):
        print("An Animal has no Sound!..")

class Tiger(animal_one):
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

'''
The issubclass(sub,sup) method
The issubclass(sub, sup) method is used to check the relationships between the specified classes.
It returns true if the first class is the subclass of the second class, and false otherwise.
'''
class Calculation1:
    def multiplication(self, a,b):
        return a*b

class Calculation2:
    def summation(self, a, b):
        return a+b

class Calculation3:
    def subtraction(self, a, b):
        return a-b

class Derived(Calculation1, Calculation2, Calculation3):
    def division(self, a, b):
        return a/b

print(issubclass(Derived, Calculation3))
print(issubclass(Calculation3, Calculation2))
print("*******************************")

'''
The isinstance (obj, class) method
The isinstance() method is used to check the relationship between the objects and classes. 
It returns true if the first parameter, i.e., obj is the instance of the second parameter, i.e., class.
'''
class Calculation1:
    def summation(self, a, b):
        return a + b

class Calculation2:
    def subtraction(self, a, b):
        return a - b

class Derived(Calculation2, Calculation1):
    def division(self, a, b):
        return a/b
    def multiplication(self, a, b):
        return a*b

d = Derived()
print(isinstance(d, Derived)) # prints true if the object d is an instance of the class Derived
print(isinstance(d, Calculation3)) # prints false

print("*******************************")

# METHOD OVER-RIDING
class Animal:
    def sound(self):
        print("An Animal has no sound!..")

class Dog(Animal):
    def sound(self):
        print("This is a Dog and it Barks!..")


d1 = Dog()
d1.sound()

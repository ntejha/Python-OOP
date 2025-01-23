# object = A "bundle" of related attributes (variables) and methods (functions).

# objects have attributes, which are like characteristics.
# objects have methods, what all they can do.

# class = (blueprint) used to design the structure and layout of an object.

# Example 01

'''
class Car :                                                    # this is how we create a class
    def __init__(self, model, year, color, for_sale):          # this is how we intialize attributes
        self.model = model                  # this is how you assign an object
        self.year = year
        self.color = color
        self.for_sale = for_sale

The above code is inside a car.py file seperately inorder to keep things neater.
Where, just an "from car import car" is enough to access the classes.

from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

# we have created two new methods "drive" and "stop", which has its own print statements
# we have used an f before the parenthsis of the print funtion inorder to call the model of the car.

car1.drive()
car1.stop()

# we have create a new method called "describe" to print the car

car1.describe() 

'''


# Class Variables

# Class variables = Shared among all instances of a class
#                   Defined outside the instialization of the class
#                   Allow you to share data among all objects created from that class

# Example 02
'''
class Student : 

    class_year = 2024    # Class variable
    num_students = 0     # Class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob",30)
student2 = Student("Patrick", 35)
student3 = Student("Squidwards", 55)
student4 = Student("Sandy", 27)

print(student2.name)
print(student2.age)
print(Student.class_year)
print(Student.num_students)
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
'''




# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

'''
class Animal:
    def __init__(self, name):
        self.name = name
        self.isalive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    
    def speak(self):
        print("WOOF!!")

class Cat(Animal):
    def speak(self):
        print("MEOW!!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Micky")

print(cat.name)
print(cat.isalive)

cat.eat()
cat.sleep()

dog.speak()

'''


# Multiple Inheritence = inherit from more than one parent class
#                        C(A,B)

# Multilevel inheritence = inherit from a parent which inherits from another parent
#                        C(B) <- B(A) <- A
'''
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"This {self.name} is eating")
    def sleep(self):
        print(f"this {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")

class Rabit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
rabbit.eat()
rabbit.sleep()

'''

# Abstract class : A class that cannot be instaniated on its own; Meant to be subclassed.
#                  They can contain abstract methods, which are declared but have no implmentation
#                  Abstract class benefits :
#                     1. Prevents instantiation of the class utslef
#                     2. Requires children to use inherited abstract methods

'''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("You stop the motorcycle")

Motorcycle = Motorcycle()

Motorcycle.go()
'''


#super() = function used in a child class to call methods from a parent class (superclass)
#          Allows you to xtend the functionality of the inherited methods

class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def Describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color,is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


circle = Circle("red",True,5)

print(circle.color)

circle.Describe()

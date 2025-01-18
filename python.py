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
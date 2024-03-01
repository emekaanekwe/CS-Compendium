#TODO: dynamic method binding?

'''
Python is multiparadigm that support classes, which are blueprints/templates
for CREATING objects (unlike Java where classes are objects)
    They work towards structuring code by having objects as
    instances, and those objects have a set f attributes (data),
    and a set of methods (functions)
    
1) Attributes - vars tat store data. they define the characteristics
    or properties of objects created from class. They're like the 
    nouns and adjectives of language

2) Methods - the actions/operations that define what the object can
    perform like the verbs

3) Four Pillars of OOP
    Encapsulation - classes cover over both data and methods to hide
        the internal details of the class from outside, which allows
        information hiding and abstraction

    Inheritance - allowing one class to inherit the attributes and
        methods of another class. This allows efficient code resue
        and hierarchies

    Polymorphism - allows objecs of different classes to be treated
        as objects of a common class. Allows dynamic method binding
        and flexibility i n function calls

    Instantiation - when an obj is created from a class, it is
        instantiated. It is calling a class AS IF it were a function
        which in turn creates an obj with its own attributes and
        methods based on the class constraints.

4) Naming Conventions
    Public Members - normal naming pattern
    Non-Public Members - _radius, _calculate_area()
        these are not meant to be a part of the class's API
        this only advises that the attribute is intended for
        use only inside the class
    Name Mangling - __<name>  are names that do not have 
        direct access, thus not part of class's API


'''

import math as mt

class Circle:
    #define and set the initial values for attributes
    #self holds a reference to the current obj so can be used inside class
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def calcArea(self):
        return round(mt.pi * self.radius ** 2, 2)


circle = Circle(5)
circle2 = Circle(10)
#simply print the memory locations of the objects
print(circle, circle2)

#simply get the argument passed
radOfC = circle.radius
print(radOfC)

#call the method that calculates the area
areaOfC = circle.calcArea()
print("area of circle:", areaOfC)

#4
publicname = 5
_nonpublicname = 10




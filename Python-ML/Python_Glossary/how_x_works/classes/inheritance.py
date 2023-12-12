'''
--REFRESHERS--

__init__ - due to the method's runtime, it CAN be considered a constructor
    it is the main rep of larger class of methods called operator overloading methods, i.e. dunder methods

polymorphism - the meaning of an operation depends on the object being operated on 
    can be used to encapsulate obj references or vars
'''

class Parent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ChildOne:
    def __init__(self, w):
        self.w = w
        Parent.__init__(self.x) #?
        

class ChildTwo:
    def __init__(self, z):
        self.z = z
        Parent.__init__(self.y) #?

class C1(): #how to link to superclass
    def __init__(self, name_obj):
        self.setName = name_obj

inst1 = C1("Atredies")
inst2 = C1("Harkonnen")

print(f"{inst1.setName}, and {inst2.setName}")
    
#TODO: NEEDS FIXING
# TODO: how extends works?
# TODO: make a regular expression command to read the words containing "ing" and return those as strings
'''
when using __init__ classes, almost all are custom
    implementations of the instance method

allows you to leave object in valid state so they
    can be used right away

__init__ is called AFTER the instance by __new__ has
    been created

in constructing objects, __new__ is used to create
    it and __init__ is used to customize it. No
    non-None value may be returned by __init__()
    
 
'''


import math as m

x = 2
y = 8
count = 2
def twoToPowerN(exponent):
    #set a var to 2 => set var to n where n=number of times 2 will be 
    # multiplied by itself => if n = 8, then increment =>
    # 2*2
    two = 2
    stopcondition = two*exponent
    for i in range(1, exponent+1):
        if i >= stopcondition:
            return stopcondition
        print(i)    
print(twoToPowerN(8))
    

class Bot:
    def __init__(self, parts, name, activate) -> None:
        #direction-number correspondence: 5=North 10=South 20=East 40=West
        self.parts = {"left-arm":1, "right-arm":2, "wheels":3}
        self.name = name
        self.activate = activate

    def turnArm(self):
        pass
        
        
class A:
    def __init__(self, bot) -> None:
        self.bot = bot
    def name(self):
        print(f"here's a {self.bot}")

bot_a = A('bot')

bot_a.name()
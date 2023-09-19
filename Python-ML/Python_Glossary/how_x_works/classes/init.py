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

x = object.__init__
y = object.__new__



print(object.__init__ == 0)

print(object)

obj = object.__dict__

print(obj)


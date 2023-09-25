'''
Intersting how if I call both of tese functions, 
the python script works like a loop
'''

#test calling funcions within other functions
def thirdTest(c):
    print("arg 3:", c)
    if c <= 10:
        print("test 3 passed")
        return 1
    else:
        print("test 3 failed")
        return 0
def secondTest(b):
    print("arg 2:", b)
    if b >= 5:
        print("test 2 passed")
        thirdTest(b)
    else:
        print("test 2 failed")
        return 0
def firstTest(a):
    print("arg 1:", a)
    if a > 0:
        print("test 1 passed")
        secondTest(a)
    else:
        print("test 1 failed")
        return 0

firstTest(11)

#test passing a function as an argument for another function
def argTwo():
    print("arg 3 passed")
def argOne(function):
    print("arg 2 passed")
def firstFunct(function):
    print("arg 1 passed")

firstFunct(argOne(argTwo()))

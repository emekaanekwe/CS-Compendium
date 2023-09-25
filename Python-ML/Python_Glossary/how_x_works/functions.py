'''
If the outer most scoped function F has dependent functions, 
outer function will execute along with dependent
functions F1...Fn before moving on to next
function R whos scope is the same as F
'''

#test calling funcions within other functions
def thirdTest(c):
    c **= 2
    print("arg 3: ", c)
    if c < 10:
        print("test 3 passed")
        return 1
    else:
        print("test 3 failed")
        return 0
def secondTest(b):
    b -= 1
    print("arg 2:", b)
    if b <= 5:
        print("test 2 passed")
        thirdTest(b)
    else:
        print("test 2 failed")
        return 0
def firstTest(a):
    a //= 2
    print("arg 1:", a)
    if a > 0:
        print("test 1 passed")
        secondTest(a)
    else:
        print("test 1 failed")
        return 0



#test passing a function as an argument for another function
def argTwo():
    print("arg 3 passed")
def argOne(argTwo):
    print("arg 2 passed")
def firstFunct(argOne):
    print("arg 1 passed")

firstTest(8) #it can take 8 and only 8 for all tests to pass
firstFunct(argOne(argTwo()))

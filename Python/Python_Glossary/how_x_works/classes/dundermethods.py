'''
dunder methods are special methods that are a
    fundamental part of python's internal 
    class mechanism

a special method (__<method name>__) is called 
    implicitly by Python to execute a certain 
    operation on a type (e.g. addition, slicing)

these methods are python's approach to Operator
    Overloading: allowing classes to define their own
    behavior.

'''

#example of special methods
def __getitem__(x, i):
    #in this case, an iterable is needed
    if x[i] == type(x).__getitem__(x, i):
        print("true")
        return 1
    else:
        print("false")
    
__getitem__([1,2,3], 2)

class NewClass:
    
    #create a new instance of a class    
    def __new__():
        pass
        
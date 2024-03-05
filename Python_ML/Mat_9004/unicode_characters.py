from collections.abc import Callable

from regex import match

import pandas as pd

class Calculus_Unicode:
    
    def __init__(self, unicode):
        self.code = ""
        #official unicode list
        self.unicode = {"alpha": "\u03b1", "integral": "\u222B"}
        
    
    def display_unicode(self):
        unicode_list = ["alpha"]
        print("Here is a list of all relevant symbols for Calculus:")
        print(unicode_list)
        print("type in an item in the list to see its corresponding symbol")
        select_item = input()
        #put codes in list
            #show otions
                #ask input (input must = option)
                    #display option
        print(self)
        
    

'''
#Print Unicodes
unicode = Calculus_Unicode
print(unicode.display_unicode("alpha -  \u03b1"))
print(unicode.display_unicode("integral - \u222B; double - \u222c; triple - \u222d"))
print(unicode.display_unicode("differential - \u2202"))
print(unicode.display_unicode("differential - \u2202"))


\u+222x
\u+223x
\u+224x
\u+225x
\u+226x
\u+227x
\u+228x
\u+229x
\u+22Ax
\u+22Bx
\u+22Cx
\u+22Dx
\u+22Ex
\u+22Fx

'''
def input_unicode_dict():
    num_response = input()
    u_dict_calculus = {1: "Integral", 2: "Differential (Leibniz)", 3: "Limit", 4: "Summation", 5: "Pi(Product)", 6: "Derivative: Prime", 7: "Derivative: Double Prime", 8: "Inequality", 9: "Infinity", 10: "Delta", 11: "Nabla/Gradient"}
    u_dict_linear_algebra = {}
    u_dict_algebra = {}
    print(len(u_dict_calculus))
    convert_num = int(num_response)
    get_i = u_dict_calculus.get(convert_num)
    print(get_i)
    #regex option
    #match_str = match("\a")
    while True:
        try:
            isinstance(convert_num, int)
        except ValueError:
            raise ValueError("Please make sure to type a number") from None
        try:
            convert_num <= len(u_dict_calculus)
        except IndexError:
            raise IndexError("Please select one of the numbers in the list")
        if u_dict_calculus.get(1) == "Integral":
            print(num_response)
        return num_response

def input_unicode_list():
    # official list of unicodes
    u_list_calculus = [[1, "Integral", "\u222b"]]
    print("Here is a list of the names of symbols commonly found in calculus:")
    for i in u_list_calculus:
        print(f"{i[0]}. {i[1]}")
    print("Type in the number below that corresponds to the Symbol you would like to see: \n")
    num_response = input()
    if num_response == str(1):
        response = int(num_response)
        print("\n", u_list_calculus[response-1][response+1], " - " + u_list_calculus[response-1][response])
    else:
        print("fail")

#input_unicode_dict()
input_unicode_list()

'''
    while input != option:
        try:
            next_guess = prev_guess - function(prev_guess) / derivative(prev_guess)
        except incorrect option:
            raise ("Could not find root") from None
        if abs(prev_guess - next_guess) < 10**-5:
            return next_guess
        prev_guess = next_guess
'''
'''
(base) emeka@emeka-20X100GCUS:~/Documents/CS-Compendium$ python3
Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> dir(Callable)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Callable' is not defined. Did you mean: 'callable'?
>>> import Callable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'Callable'
>>> from collections.abc import Callable
>>> dir(Callable)
['__abstractmethods__', '__call__', '__class__', 
'__class_getitem__', '__delattr__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getstate__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', 
'__le__', '__lt__', '__module__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', 
'__slots__', '__str__', '__subclasshook__', 
'_abc_impl']
'''
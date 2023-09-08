import pandas as pd
from underscores_private import _a, _b, _private_function
#TODO: what is bulletin module?
'''
_ is used in the interactive interpreter to store the result
    of the last evaluation.

--Different kinds of underscores--
_           customary to use as a dummy var
abc_        allows reserved keywords o be var names 
_abc        makes values of vars hidden/private and are not available
                externally unless called upon. first the file where
                var/funct is needs to be imported
__abc__     Dunder class methods. Can be used as constructors
__abc       name mangling: process that alters the name of a class attribute
                to avoid unintentional verriding. used to avoid name clashing
                
    

Cases:

1. unused vars - indicate that value of var will not be used

2. internalization and localization - 
'''

#unused/dummy var that is overwritten and the last time
    #it got assigned remains in memory
for _ in range(3):
    print("_ is for an unused var")
#Often used in ML and typing large nums
large_num = 1_000_000_000 #9 zeros
print(large_num)

#reserved keywords to vars
class_ = "class keyword is now a var"
print(class_)

#hidden/private vars & functs
#prefer to list what is imported rather than using *
print(_a, _b)
_private_function()

#__name__ and __main__ are special vars that are related to 
    #script execution and module import. helps determine
    #whether a py script is being run as the main program
    #or imported as module
#__name__ exists in every module. when module is imported into
    #another script, __name__ is set to name of module. if a script
    #is executed expilcitly, the defaults to __main__
if __name__ == "__main__":
    print("this file's __name__ is set to: ", __name__)

class ClassOne:
    def __init__(self) -> None:
        pass
    
class ClassTwo:
    def __init__(self) -> None:
        pass

    
    
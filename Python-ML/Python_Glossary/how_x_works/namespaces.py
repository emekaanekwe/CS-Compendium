'''
Namespaces: a collection of currently defined symbolic names along with info about the obj
    that each name references. namespaces are like dictionaries where key=obj name and value=the obj itself

Types:
1. Built-in     predefined objs
2. Global       objs belonging to main program, any module using import, main func
3. Local        new namespace when funct executes and remains in funct until funct termination
4. Enclosing    the namespace of obj/funct that encloses local namespaces but still resides in another funct
each with its own lifetime in the program

Built-In(Global(Enclosing(Local())))
'''

#print obj with built-in namespaces
print(dir(__builtins__))

#global namespaces are made for any module that the program loads
x = 'global'
print("x here is", x)
def f():
    x = 'enclosing'
    print("x within f() here is", x)
    def g():
        x = 'local'
        print("x within g() here is", x)
    g()
f()
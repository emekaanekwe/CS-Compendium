'''
Tuples is an immutable sequence type, typically used to store collections of heterogeneous data 
(such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for 
cases where an immutable sequence of homogeneous data is needed (such as allowing 
storage in a set or dict instance).



['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
'__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
'__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']]
'''


ex_tuple = (1, 2, 3, 4, 5)
print(ex_tuple)

#empty tuple
empty_tuple = ()
print(dir(empty_tuple))

#built-in method
ex_list = [1, 2, 3]
print(tuple(ex_list))




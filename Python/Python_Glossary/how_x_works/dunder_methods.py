'''
Python dunder methods, also known as special methods or magic methods, are used for operator overloading, customizing behavior for built-in operations, and creating user-defined classes that emulate built-in types. Here's a list of all dunder methods in Python:

1. `__init__(self[, ...])`: Constructor, called when an instance of the class is created.
2. `__del__(self)`: Destructor, called when an instance is about to be destroyed.
3. `__repr__(self)`: Called by the `repr()` built-in function to compute the "official" string representation of an object.
4. `__str__(self)`: Called by the `str()` built-in function and `print()` function to compute the "informal" or printable string representation of an object.
5. `__format__(self, format_spec)`: Called by the `format()` built-in function and `str.format()` method to format the object into a formatted string.
6. `__hash__(self)`: Called by the built-in `hash()` function to compute the hash value of an object.
7. `__bool__(self)`: Called by the built-in `bool()` function to compute the truth value of an object.
8. `__lt__(self, other)`: Called by the `<` operator to implement behavior for less than comparisons.
9. `__le__(self, other)`: Called by the `<=` operator to implement behavior for less than or equal to comparisons.
10. `__eq__(self, other)`: Called by the `==` operator to implement behavior for equality comparisons.
11. `__ne__(self, other)`: Called by the `!=` operator to implement behavior for inequality comparisons.
12. `__gt__(self, other)`: Called by the `>` operator to implement behavior for greater than comparisons.
13. `__ge__(self, other)`: Called by the `>=` operator to implement behavior for greater than or equal to comparisons.
14. `__getattr__(self, name)`: Called when an attribute lookup fails (i.e., when an attribute is not found).
15. `__setattr__(self, name, value)`: Called when an attribute assignment is attempted.
16. `__delattr__(self, name)`: Called when an attribute deletion is attempted.
17. `__dir__(self)`: Called by the `dir()` built-in function to compute the list of attributes of an object.
18. `__getattribute__(self, name)`: Called whenever an attribute is accessed.
19. `__setitem__(self, key, value)`: Called to implement assignment to an item.
20. `__getitem__(self, key)`: Called to implement evaluation of self[key].
21. `__delitem__(self, key)`: Called to implement deletion of self[key].
22. `__iter__(self)`: Called when an iterator is required for the object.
23. `__next__(self)`: Called to implement the next item of the iterator.
24. `__reversed__(self)`: Called by the `reversed()` built-in function to implement reverse iteration.
25. `__contains__(self, item)`: Called by the `in` and `not in` operators to implement membership tests.
26. `__len__(self)`: Called by the `len()` built-in function to compute the length of the object.
27. `__length_hint__(self)`: Called by the `len()` built-in function to obtain an estimated length.
28. `__add__(self, other)`: Called by the `+` operator to implement behavior for addition.
29. `__sub__(self, other)`: Called by the `-` operator to implement behavior for subtraction.
30. `__mul__(self, other)`: Called by the `*` operator to implement behavior for multiplication.
31. `__matmul__(self, other)`: Called by the `@` operator to implement behavior for matrix multiplication (Python 3.5+).
32. `__truediv__(self, other)`: Called by the `/` operator to implement behavior for true division.
33. `__floordiv__(self, other)`: Called by the `//` operator to implement behavior for floor division.
34. `__mod__(self, other)`: Called by the `%` operator to implement behavior for modulus.
35. `__divmod__(self, other)`: Called by the `divmod()` built-in function to implement behavior for floor division and modulus.
36. `__pow__(self, other[, modulo])`: Called by the `**` operator to implement behavior for exponentiation.
37. `__lshift__(self, other)`: Called by the `<<` operator to implement behavior for left bitwise shift.
38. `__rshift__(self, other)`: Called by the `>>` operator to implement behavior for right bitwise shift.
39. `__and__(self, other)`: Called by the `&` operator to implement behavior for bitwise AND.
40. `__xor__(self, other)`: Called by the `^` operator to implement behavior for bitwise XOR.
41. `__or__(self, other)`: Called by the `|` operator to implement behavior for bitwise OR.
42. `__radd__(self, other)`: Called by the `+` operator when the left operand does not support addition (i.e., reverse addition).
43. `__rsub__(self, other)`: Called by the `-` operator when the left operand does not support subtraction (i.e., reverse subtraction).
44. `__rmul__(self, other)`: Called by the `*` operator when the left operand does not support multiplication (i.e., reverse multiplication).
45. `__rmatmul__(self, other)`: Called by the `@` operator when the left operand does not support matrix multiplication (i.e., reverse matrix multiplication) (Python 3.5+).
46. `__rtruediv__(self, other)`: Called by the `/` operator when the left operand does not support true division (i.e., reverse true division).
47. `__rfloordiv__(self, other)`: Called by the `//` operator when the left operand does not support floor division (i.e., reverse floor division).
48. `__rmod__(self, other)`: Called by the `%` operator when the left operand does not support modulus (i.e., reverse modulus).
49. `__rdivmod__(self, other)`: Called by the `divmod()` built-in function when the left operand does not support floor division and modulus (i.e., reverse divmod()).
50. `__rpow__(self, other[, modulo])`: Called by the `**` operator when the left operand does not support exponentiation (i.e., reverse exponentiation).
51. `__rlshift__(self, other)`: Called by the `<<` operator when the left operand does not support left bitwise shift (i.e., reverse left bitwise shift).
52. `__rrshift__(self, other)`: Called by the `>>` operator when the left operand does not support right bitwise shift (i.e., reverse right bitwise shift).
53. `__rand__(self, other)`: Called by the `&` operator when the left operand does not support bitwise
'''
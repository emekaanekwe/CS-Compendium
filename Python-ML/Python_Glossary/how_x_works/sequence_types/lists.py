'''
sequence types: lists, tuples, range

to explore how exactly .append() works
from: https://github.com/python/cpython/blob/2396614b8958ad202378fd71a598eb4106ac5896/Objects/listobject.c#L838
static PyObject *
list_append(PyListObject *self, PyObject *object)
/*[clinic end generated code: output=7c096003a29c0eae input=43a3fe48a7066e91]*/
{
    if (app1(self, object) == 0)
        Py_RETURN_NONE;
    return NULL;
}

>>Legal Operations Over Mutable Seuqnce Types

Operation                   Result

s[i] = x                    item i of s is replaced by x

s[i:j] = t                  slice of s from i to j is replaced by the contents of the iterable t

del s[i:j]                  same as s[i:j] = []

s[i:j:k] = t                the elements of s[i:j:k] are replaced by those of t

del s[i:j:k]                removes the elements of s[i:j:k] from the list

s.append(x)                 appends x to the end of the sequence (same as s[len(s):len(s)] = [x])

s.clear()                   removes all items from s (same as del s[:])

s.copy()                    creates a shallow copy of s (same as s[:])

s.extend(t) or s += t       extends s with the contents of t (for the most part the same as s[len(s):len(s)] = t)

s *= n                      updates s with its contents repeated n times

s.insert(i, x)              inserts x into s at the index given by i (same as s[i:i] = [x])

s.pop() or s.pop(i)         retrieves the item at i and also removes it from s

s.remove(x)                 remove the first item from s where s[i] is equal to x

s.reverse()                 reverses the items of s in place

'''

li_empty = []
li_1 = [1, 2, 3, 4, 5]
li_2 = ["six"]
#li_2 = li_1 + 6 <- cannot concat int and str
print(dir(li_empty))
print(len(li_1))
def __getitem__ (x):
    x = [1,2,3,4]
    pass
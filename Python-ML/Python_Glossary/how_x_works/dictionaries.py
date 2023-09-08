#TODO: missing keys class?
#TODO: how does iterator work?
#TODO: classmethod fromkeys(iterable[, value])?
#TODO: print(dict.get("key four"[1]))?
#TODO: po = dict.pop("key four"[1])?
#TODO: d | other? d|= other?
'''
mutable, dynamic and nested key-value pairs
they can contain lists
'''

#define a dictionary
dict = {
    "key one" : 5,
    "key two" : 10,
    "key three" : 20
}
print(dir(dict))
print("\n\n\n")
print(dict)

#another way to write
print({x: x + 5 for x in range(10)})

#use type constructor
#dict([('one', 1), ('two', 2), ('three', 3)])
#my_dict = dict([('one', 1), ('two', 2)])
#dict(one=1, two=2)

#--Common Methods--

#return list of all keys
li = list(dict)
print("the keys of dict: ", li)

#return number of items
le = len(dict)
print("number of items in dict: ", le)

#return item of dict with the key
print("what's returned when calling key one: ", dict["key one"])

#counter and checks for missing keys
'''class Counter(dict):
    def __missing__(self, key):
        return 0
c = Counter()
c['red']

c['red'] += 1
c['red']
'''
#setting a vlue to a key
dict["key one"] = 40
print("new value for key one: ", dict["key one"])

#return true if dict has key, else false
print("key one" in dict)
print("key four" in dict)
#can also use
print("key one" not in dict)

#return an iterat over the keys
it = iter(dict)
print(it)

#remove all items
cl = dict.clear()
print("dict cleared. ", cl)

#copy a dict
dict = {"key four": 80, "ley five" : 160, "key six" : 320}
print("new dict: ", dict)
dict_copy = dict.copy()
print("dict copied: ", dict_copy)

#return value of key. if default not given => None
print(dict.get("key four"[1]))

#new view of items
print("new view of items: ", dict.items())

print("new view of keys: ", dict.keys())

#remove key and return value, else return default


#remove and return k:v pair in LIFO order
popit = dict.popitem()
print("removed item from dict in LIFO order: ", popit)

#return reverse iterator over the keys
re = reversed(dict)
print(re)

#make some new items
dict["key seven"] = 720
#return new view of values
print("new view of values: ", dict.values())
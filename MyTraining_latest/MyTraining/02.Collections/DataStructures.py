"""
Data Structures (list, dict, tuples, sets):-
Python have the following builtins data structures
    1)lists, tuples, dictionaries, strings, sets and frozensets.

List and tuples are like arrays. In list/tuple we can store heterogeneous objects.ie we can store any type
objects.
"""

print("\n==========================Lists Info=================")   
list1 = ['Hello',2,3,3,'baig']
print(list1)
#lists are mutable you can add values to lists
list1[0]=3
print(list1)
#Iteration
for value in list1:
    print(value)

"""
Output:-
== == == == == == == == == == == == == Lists Info == == == == == == == == =
['Hello', 2, 3, 3, 'baig']
[3, 2, 3, 3, 'baig']
3
2
3
3
baig
"""

print("==========================Tuples Info=================")
tuple1 = ('Hello',2,3,'baig')
print(tuple1)
print(tuple1[0])
#tuples are immutable , Once tuple is created you cannot add values to tuples
#tuple1[0]=20 if try to add values it throws the following TypeError
#TypeError: 'tuple' object does not support item assignment
#Iteration
for value in tuple1:
    print(value)

"""
Output:-
==========================Tuples Info=================
('Hello', 2, 3, 'baig')
Hello
Hello
2
3
baig
"""

#Sets store unique elements ,Sets are muttable whereas frozensets are immutable sets.

print("\n==========================sets Info=================")   
set1 = {1,2,3,3}
print(set1)
#set remove duplicates
#sets are mutable you can add values to sets. But since they are unordered, indexing have no meaning.
#set1[0]=4 #We cannot access or change an element of set using indexing or slicing. Set does not support it.
set1.add(5) # by using add method we can add values to set
print(set1)
#Iteration
for value in set1:
    print(value)

"""
Output:-
==========================sets Info=================
{1, 2, 3}
{1, 2, 3, 5}
1
2
3
5

"""

print("\n==========================forzensets Info=================")  
#Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. 
#While tuples are immutable lists, frozensets are immutable sets.
fset1 = frozenset({1,2,3,3})#
print(fset1)
#fset1.add(5) # we cannot add values to forzenset AttributeError: 'frozenset' object has no attribute 'add'
#Iteration
for value in fset1:
    print(value)

"""
Output:-
== == == == == == == == == == == == == forzensets Info == == == == == == == == =
frozenset({1, 2, 3})
1
2
3
"""

#Dictionary stores name value pairs. i.e each item is a pair made of a key and a value.
#Like set, dictionaries are also not sorted. you can access keys and values independently.
print("\n==========================dictionary Info=================")   
dict1 = {'eid1':100,'eid2':101, 'eid1':105}
print(dict1)
#above print method prints {'eid2': 101, 'eid1': 105}  because u r adding same key twice,so last values is updated in the key.
print(dict1.items())
print(dict1.keys())
print(dict1.values())
#Iteration
for value in dict1.values():
    print(value)

"""
Output:-
==========================dictionary Info=================
{'eid2': 101, 'eid1': 105}
dict_items([('eid2', 101), ('eid1', 105)])
dict_keys(['eid2', 'eid1'])
dict_values([101, 105])
101
105
"""


"""
When to use a dict/list/tuple/set ????

When to use a dictionary:
– When you need a logical association between a key:value pair.
– When you need fast lookup for your data, based on a custom key.
– When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
– Use lists if you have a collection of data that does not need random access.
      Try to choose lists when you need a simple, iterable collection that is modified frequently.
– Use a set if you need uniqueness for the elements.
– Use tuples when your data cannot change.

Many times, a tuple is used in combination with a dictionary, for example,
a tuple might represent a key, because it’s immutable.
"""

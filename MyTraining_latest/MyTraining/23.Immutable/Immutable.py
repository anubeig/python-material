"""
Common immutable type:

numbers: int(), float(), complex()
immutable sequences: str(), tuple(), frozenset(), bytes()
Common mutable type (almost everything else):

mutable sequences: list(), bytearray()
set type: set()
mapping type: dict()
classes, class instances
etc.
One trick to quickly test if a type is mutable or not, is to use id() built-in function.
"""

Examples, using on integer,

>>> i = 1
>>> id(i)
***704
>>> i += 1
>>> i
2
>>> id(i)
***736 (different from ***704)
using on list,

>>> a = [1]
>>> id(a)
***416
>>> a.append(2)
>>> a
[1, 2]
>>> id(a)
***416
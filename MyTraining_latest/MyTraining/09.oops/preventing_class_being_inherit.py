#To do this for custom Python classes, use a metaclass:
class Final(type):
    def __new__(cls, name, bases, classdict):
        for b in bases:
            if isinstance(b, Final):
                raise TypeError("type '{0}' is not an acceptable base type".format(b.__name__))
        return type.__new__(cls, name, bases, dict(classdict))

class Foo:
    __metaclass__ = Final

class Bar(Foo):
    pass

"""
gives
>>> class Bar(Foo):
...     pass
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in __new__
TypeError: type 'Foo' is not an acceptable base type
"""
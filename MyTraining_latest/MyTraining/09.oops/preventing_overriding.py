"""
There really aren't any true "private" attributes or methods in Python. One thing you can do is simply ' \
                 'override the method you don't want in the subclass, and raise an exception:
"""
>>> class Foo( object ):
...     def foo( self ):
...         print 'FOO!'
...
>>> class Bar( Foo ):
...     def foo( self ):
...         raise AttributeError( "'Bar' object has no attribute 'foo'" )
...
>>> b = Bar()
>>> b.foo()
Traceback (most recent call last):
  File "<interactive input>", line 1, in <module>
  File "<interactive input>", line 3, in foo
AttributeError: 'Bar' object has no attribute 'foo'
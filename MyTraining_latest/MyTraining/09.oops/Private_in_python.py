"""lets make bar private. We can do that by adding two leading underscores to the name."""


class Foo:
    def __init__(self):
        self.__bar = 1


foo = Foo()
# print foo.__bar
"""
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    print foo.__bar
AttributeError: Foo instance has no attribute '__bar'
"""

"""
What has happened here is that the name of __bar  has been changed by the
interpreter so that it is not easily accessible outside the class. If we take a look at __dict__  again,
we will see that it has been renamed to _Foo__bar , and can be accessed and assigned using that name.
"""
print foo.__dict__

print foo._Foo__bar

"""
We only have to use the mangled name outside the class. Inside, we access the attribute in the normal way.
"""


class Foo(object):
    def __init__(self):
        self.__bar = 1

    def bar(self):
        return self.__bar


print Foo().bar()

"""
GETTERS AND SETTERS
After learning about private attributes, sometimes new Python programmers get the idea
that they can use getters and setters to manage accessing and assigning attributes,
so they write something like this
"""


class Foo(object):
    def __init__(self):
        self.__bar = 1

    def get_bar(self):
        return self.__bar

    def set_bar(self, value):
        self.__bar = value


foo = Foo()
print foo.get_bar()

foo.set_bar(2)
print foo.get_bar()

"""
PRIVATE METHODS

Methods can be made private in the same way, by naming them with two leading underscores and no trailing underscores.
"""


class Foo(object):
    def __init__(self):
        self.__hello = "Hello"

    def __say_hello(self):
        print(self.__hello)

    def say_hello(self):
        self.__say_hello()


foo = Foo()
foo.say_hello()

foo.__say_hello()
"""
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    foo.__say_hello()
AttributeError: 'Foo' object has no attribute '__say_hello'
"""



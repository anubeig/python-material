"""
First of all, we need to create a class that we can play with.
Here’s a simple class that doesn’t do much of anything:
"""

class Mutable(object):
    """
    A mutable class
    """

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass


mut_obj = Mutable()
mut_obj.monkey = "tamarin"
print mut_obj.monkey

"""
This class does allow us to add attributes to it at run time.
Now that we know how to do some simple monkey patching, let’s try to block that behavior.
"""

"""
Creating an 23.Immutable Class

One of the examples I was reading about immutable classes mentioned that
you could create one by replacing a class’s __dict__ with __slots__. Let’s see how that looks:
"""


class Immutable(object):
    """
    An immutable class
    """
    __slots__ = ["one", "two", "three"]

    # ----------------------------------------------------------------------
    def __init__(self, one, two, three):
        """Constructor"""
        super(Immutable, self).__setattr__("one", one)
        super(Immutable, self).__setattr__("two", two)
        super(Immutable, self).__setattr__("three", three)

    # ----------------------------------------------------------------------
    def __setattr__(self, name, value):
        """"""
        msg = "'%s' has no attribute %s" % (self.__class__,
                                            name)
        raise AttributeError(msg)


"""
Now we just need to create an instance of this class to see if we can monkey patch it:
"""

i = Immutable(1, 2, 3)
i.four = 4

"""
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
AttributeError: '23.Immutable' object has no attribute 'four'
"""
"""
In this case, the class does not allow us to monkey patch the instance.
Instead, we receive an AttibuteError. Let’s try to change one of the attributes:
"""

i = Immutable(1, 2, 3)
i.one = 4
"""
This is because we have overridden the __setattr__ method.
You could just override the method and not do anything at all if you wanted.
This would stop the traceback from happening, but also prevent the value from being changed.
If you like to be explicit with what is going on, raising an error is probably the way to go.
"""


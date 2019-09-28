import gc

class MyClass(object):
    def __del__(self):
        print "del"
        pass
my_ref = MyClass()
#my_ref.ref = my_ref
del my_ref
print gc.collect()
print gc.garbage

"""
sh-4.3$ python main.py
del
0
[]
"""

"""
Circular reference
"""

import gc

class MyClass(object):
    def __del__(self):
        print "del"
        pass
my_ref = MyClass()
my_ref.ref = my_ref
del my_ref
print gc.collect()
print gc.garbage

"""
sh-4.3$ python main.py
2
[<__main__.MyClass object at 0x7efcf8dc7ed0>]




gc.garbage returns a list of uncollectable objects
(objects that are marked as unreachable but cannot be collected)
which now contains the object we tried to delete.
"""

"""
One of the more convenient aspects of writing code in interpreted languages such as Python or Ruby is that
you normally can avoid dealing with memory management. 
However, one known case where Python will definitely leak memory is
when you declare circular references in your object declarations and 
implement a custom __del__ destructor method in one these classes.
For instance, consider the following example:
"""

class A(object):
    def __init__(self, b_instance):
      self.b = b_instance

class B(object):
    def __init__(self):
        self.a = A(self)
    def __del__(self):
        print "die"

def test():
    b = B()

test()

"""
When the function test() is invoked, it declares an instance of B, which passes itself to A, which then sets a reference to B, resulting in a circular reference.
Normally Python's garbage collector, which is used to detect these types of cyclic references, would remove it.
However, because of the custom destructor (the __del__ method),
it marks this item as "uncollectable". By design, it doesn't know the order in which to destroy the objects, so leaves them alone
"""

"""
Deep Copy and Shallow copy are the two ways in which a variable is copied.

Deep Copy : When the copied variable is has its own memory location. Now changes made on deeply copied variable
            will not affect the original one.

Shallow Copy: The new variable refers to the original variable.
             In this case, if the new one altered the changes are reflected on the original variable as well.
"""
import copy

class A(object):
    a = 20
    pass

a =A();
print(a.a)
a1 = copy.copy(a)

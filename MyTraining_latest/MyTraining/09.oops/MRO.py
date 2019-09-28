class A(object):
    pass

class B(A):
    pass

class C(A):
    def who_am_i(self):
        print("I am a C")

class D(B,C):
    pass

d1 = D()
d1.who_am_i()

"""
So in our example, algorithm search path is : D, B, A, C, A.
A class cannot appears twice in search path, so the final version is D, B, A, C:

Looking in D
If not found, looking in B
If not found, looking un B first parent A
If not found, going back in B others parents (none)
If not found, looking in D others parents : C


This is due to the old classes MRO algorithm behaviour. It is a very simple and easy to understand algorithm :
When a class inherits from multiple parents, Python build a list of classes to search for when it needs to resolve which method has to be called when one in invoked by an instance.
This algorithm is a tree routing, and works this way, deep first, from left to right :
1. Look if method exists in instance class
2. If not, looks if it exists in its first parent, then in the parent of the parent and so on
3. If not, it looks if current class inherits from others classes up to the current instance others parents.
"""
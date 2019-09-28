class MyClass:
    a = 20
    def __eq__(self, other) :
        print("eq method is called")
        return self.__dict__ == other.__dict__
    pass

a1 = MyClass()
a2 = MyClass()

print(a1==a2)

print(a1 == a2)

a1.a = 30

print(a1 == a2)

"""
sh-4.3$ python3 main.py
eq method is called
True
eq method is called
False
"""

"""
here is a simple rule of thumb to tell you when to use == or is.

== is for value equality. Use it when you would like to know if two objects have the same value.
is is for reference equality. Use it when you would like to know if two references refer to the same object.
"""
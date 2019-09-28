A very simple example of __slot__ attribute.

Problem: Without __slots__

If I don't have __slot__ attribute in my class, I can add new attributes to my objects.

class Test:
    pass

obj1=Test()
obj2=Test()

print(obj1.__dict__)  #--> {}
obj1.x=12
print(obj1.__dict__)  # --> {'x': 12}
obj1.y=20
print(obj1.__dict__)  # --> {'x': 12, 'y': 20}

obj2.x=99
print(obj2.__dict__)  # --> {'x': 99}
If you look at example above, you can see that obj1 and obj2 have their own x and y attributes and python has also created a dict attribute for each object (obj1 and obj2).

Suppose if my class Test has thousands of such objects? Creating an additional attribute dict for each object will cause lot of overhead (memory, computing power etc.) in my code.

Solution: With __slots__

Now in the following example my class Test contains __slots__ attribute. Now I can't add new attributes to my objects (except attribute x) and python doesn't create a dict attribute anymore. This eliminates overhead for each object, which can become significant if you have many objects.

class Test:
    __slots__=("x")

obj1=Test()
obj2=Test()
obj1.x=12
print(obj1.x)  # --> 12
obj2.x=99
print(obj2.x)  # --> 99

obj1.y=28
print(obj1.y)  # --> AttributeError: 'Test' object has no attribute 'y'
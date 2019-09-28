#https://www.dotnetperls.com/type-python
#https://teamtreehouse.com/community/so-what-does-setattr-and-getattr-actually-do

class myobj():
    pass

dict1 = {"name":"Anubeig", "age":100}

for key,value in dict1.items():
    setattr(myobj, key, value)

print myobj.name
print myobj.age

for key in dict1.keys():
    print getattr(myobj, key)

print hasattr(myobj, "name")

print delattr(myobj, "name")

print hasattr(myobj, "name")

#print delattr(myobj, "name")

"""
sh-4.3$ python main.py
Anubeig
100
100
Anubeig
True
None
False
Traceback (most recent call last):
  File "main.py", line 21, in <module>
    print delattr(myobj, "name")
AttributeError: class myobj has no attribute 'name'
"""

print dir()
print vars()

"""

['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'dict1', 'key', 'myobj', 'value']
{'dict1': {'age': 100, 'name': 'Anubeig'}, '__builtins__': <module '__builtin__' (built-in)>, '__file__': 'main.py', 'value': 'Anubeig', '__package__': None, 'key': 'name', 'my
obj': <class __main__.myobj at 0x7f6b819cb530>, '__name__': '__main__', '__doc__': None}
"""
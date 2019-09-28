def fun():
    a = 10
    pass

print(fun.__doc__)

print(dir())

print(vars())

"""
sh-4.3$ python3 main.py
None
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fun']
{'__cached__': None, '__builtins__': <module 'builtins' (built-in)>, '__loader__': <_frozen_importlib.SourceFileLoader object at 0x7f0e4b2dc9e8>, '__package__': None, '__doc__': None, '__name__': '__main__', '__spec_
_': None, 'fun': <function fun at 0x7f0e4b3d6bf8>, '__file__': 'main.py'}
"""
import sys

# KeyError
try:
    dict1 = {"name": "Anubeig"}
    print(dict1['nam'])
except Exception as e:
    print ("Exception raise")
    print(e)  # print invalid key "nam"

# print(dict1['nam'])
"""
Traceback (most recent call last):
  File "main.py", line 8, in <module>
    print(dict1['nam'])
KeyError: 'nam'
"""

# AttributeError

try:
    print("try")
    aint = 8
    aint.append(9)
except Exception as e:
    print("Exception raise")
    print(e)

# valueError

try:
    c = float("21 C")
except ValueError as e:
    print("Exception raise")
    print(e)

# UnboundLocalError

a = 1


def fun():
    try:
        print(a)
        a += 1
    except UnboundLocalError as e:
        print("raise exception")
        print(e)


fun()


def foo():
    try:
        foo()
    except RuntimeError as e:
        print("raise exception")
        # sys.setrecursionlimit(2)
        # foo()
        print(e)


foo()

"""
sh-4.3$ python3 main.py
Exception raise
'nam'
try
Exception raise
'int' object has no attribute 'append'
Exception raise
could not convert string to float: '21 C'
raise exception
local variable 'a' referenced before assignment
raise exception
maximum recursion depth exceeded
"""
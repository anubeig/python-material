class A(object):
    def __init__(self):
        print "init"
        pass

    def __new__(cls, *args, **kwargs):
        print "Creating Instance"
        instance = super(A, cls).__new__(cls, *args, **kwargs)
        return instance


A()

"""
sh-4.3$ python main.py
Creating Instance
init
"""


class A(object):
    def __init__(self):
        print "init"
        pass

    def __new__(cls, *args, **kwargs):
        print "new"
        pass


A()
"""
sh-4.3$ python main.py
new
"""

"""
Things to remember

If __new__ return instance of  it’s own class, then the __init__ method of newly created instance
will be invoked with instance as first (like __init__(self, [, ….]) argument following by arguments passed
to __new__ or call of class.  So, __init__ will called implicitly.

If __new__ method return something else other than instance of class,
 then instances __init__ method will not be invoked. In this case you have to call __init__ method yourself.
"""
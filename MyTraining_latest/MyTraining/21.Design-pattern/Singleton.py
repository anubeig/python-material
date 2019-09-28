w   lass Singleton(object):
    _instance = None  # Keep instance reference

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


s1 = Singleton()
s2 = Singleton()
if s1 == s2:
    print "same"


class A():
    pass

"""
output : same
"""

s1 = A()
s2 = A()

if s1 == s2:
    print "same"
else:
    print "Not same"

"""
output : Not same
"""
def func(*args):
    print args[0]
    print args[1]
    pass

func(2,3)

def func(*args):
    return args

args = func(2,3)
print args[0]
print args[1]

"""
Usage of **kwargs
**kwargs allows you to pass keyworded variable length of arguments to a function.
You should use **kwargs if you want to handle named arguments in a function.
 Here is an example to get you going with it:
"""
def greet_me(**kwargs):
    print args
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "%s == %s" %(key,value)

nvp = {'name' : 123}
greet_me(name="yasoob")

"""
where as *args used for list
where as ***kwargs is used for name value pairs
"""

"""
Using *args and **kwargs to call a function
So here we will see how to call a function using *args and **kwargs. Just consider that you have this little function:
"""

def test_args_kwargs(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

# first with *args
args = ("two", 3,5)
test_args_kwargs(*args)

# now with **kwargs:
kwargs = {"arg3": 3, "arg2": "two","arg1":5}
test_args_kwargs(**kwargs)

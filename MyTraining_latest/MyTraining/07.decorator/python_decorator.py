#https://www.programiz.com/python-programming/decorator
#https://realpython.com/blog/python/primer-on-python-decorators/
#http://www.bogotobogo.com/python/python_decorators.php

"""
 Decorators provide a simple syntax for calling higher-order functions.
 By definition, a decorator is a function that takes another function and
 extends the behavior of the latter function without explicitly modifying it.

def myFunction(in_function):
   def out_function():
      pass
   return out_function
The myFunction is indeed a decorator because by definition a decorator is a function that
takes a function object as its argument, and returns a function object.
"""


def my_decorator(some_function):
    def wrapper():

        num = 10

        if num == 10:
            print("Yes!")
        else:
            print("No!")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")


"""
just_some_function = my_decorator(just_some_function)

just_some_function()
"""


@my_decorator
def just_some_function():
    print("Wheee!")


just_some_function()


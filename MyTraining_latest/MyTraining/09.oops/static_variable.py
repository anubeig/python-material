class Foo(object):
  # Class variable, shared by all instances of this class
  counter = 0

  def __call__(self):
    Foo.counter += 1
    print Foo.counter

# Create an object instance of class "Foo," called "foo"
foo = Foo()

# Make calls to the "__call__" method, via the object's name itself
foo() #prints 1
foo() #prints 2
foo() #prints 3

"""
python doesn't have static variables but you can fake it by defining a callable class object and then using it as a function. 
"""
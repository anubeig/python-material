class ValueTooSamll(Exception):
    pass

try:
    raise ValueTooSamll("Too small")
except Exception as e:
    print(e)



# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()

print("Congratulations! You guessed it correctly.")


"""
With modern Python Exceptions, you don't need to abuse .message, or override .__str__() or .__repr__() 
or any of it.
If all you want is an informative message when your exception is raised, do this:

class MyException(Exception):
    pass

raise MyException("My hovercraft is full of eels")
That will give a traceback ending with MyException: My hovercraft is full of eels.

If you want more flexibiilty from the exception, you could pass a dictionary as the argument:

raise MyException({"message":"My hovercraft is full of animals", "animal":"eels"})
However, to get at those details in an except block is a bit more complicated; they are stored in the args attribute, which is a list. You would need to do something like this:

try:
    raise MyException({"message":"My hovercraft is full of animals", "animal":"eels"})
except MyException as e:
    details = e.args[0]
    print(details["animal"])
It is still possible to pass in multiple items into the exception, but this will be deprecated in the future. 
If you do need more than a single piece of information, then you should consider fully subclassing Exception.
"""


class ValueTooSamll(Exception):
    pass

try:
    raise ValueTooSamll({"message":"Too small"})
except Exception as e:
    print(e.args[0])
    details = e.args[0]
    print(details['message'])




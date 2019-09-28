#Note:- in python method overloading is not possible directly i.e two or more functions name with different no of parameters
class Example(object):
    def add(self,a, b):
        print("Hello")

    def add(self,a, b, c):
        print("Bye")

obj = Example()
print(obj.add(4, 5))

"""
Above program throw below error:
Traceback (most recent call last):
  File "C:/Users/AM186061/PycharmProjects/MyTraining/Overloading.py", line 10, in <module>
    print(obj.add(4, 5))
TypeError: add() missing 1 required positional argument: 'c'
"""


#In Python you can define a method in such a way that there are multiple ways to call it.
#Given a single method or function, we can specify the number of parameters ourself.
class Human:
    def sayHello(self, name=None):

        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')

# Create instance
obj = Human()

# Call the method
obj.sayHello()

# Call the method with a parameter
obj.sayHello('Guido')

#then there are folks who are more than willing to say, ‘Oh! Python supports all!’ Yes, Python supports overloading but in a Pythonic way. Here’s an example,
def add(instanceOf, *args):
    if instanceOf == 'int':
        result = 0
    if instanceOf == 'str':
        result = ''
    for i in args:
        result = result + i
    return result


print(add('int', 3, 4, 5))
print(add('str', 'I', ' am', ' in', ' Python'))


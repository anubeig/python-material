class Example(object):
    i = 3
    @staticmethod
    def display():
        print("Hello")
        pass
    def print(self):
        print("Chalo")
e = Example()
print(e.i)
e.i= e.i + 1
e.display()
Example.display()
e1 = Example()
print(e1.i)
print(Example.i)
Example.i = 5
print(e1.i)
e.print()
#Example.print() -- throw runtime error TypeError: print() missing 1 required positional argument: 'self'
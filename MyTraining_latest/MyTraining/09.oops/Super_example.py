class Example(object):
    def __init__(anu):
        pass
    def display(anu):
        print("Hello")
        pass
e = Example()
e.display()

class Example(object):
    def __init__(anu):
        print("I am super class")
        pass
class Example02(Example):
    def __init__(anu):
        super().__init__()
        print("I am child")
        pass
e = Example02()


class A(object):
    def fun(self):
        print("I am parent")
        pass
class B(A):
    def fun(self):
        super().fun()
        print("I am child")
        pass

b = B()
b.fun()

"""
I am parent
I am child
"""
class Parent01(object):
    def foo(self):
        print("Parent01")
        pass

class Parent02(object):
    def foo(self):
        print("Parent02")
        pass

class Child(Parent01,Parent02):
    def foo(self):
        print("Child")
        super().foo()
    pass

c = Child()
c.foo()


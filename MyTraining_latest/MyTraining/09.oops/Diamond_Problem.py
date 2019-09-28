class A(object):
    def display(self):
        print("Parent")
        pass
class B(A):
    def display(self):
        print("B")
        pass
class C(A):
    def display(self):
        print("C")
        pass
class D(C,B):
    def display(self):
        print("D")
        super().display()
        pass

d = D()
d.display()


class A(object):
    def m(self):
        print("m of A called")

class B(A):
    pass

class C(A):
    def m(self):
        print("m of C called")


class D(B, C):
    pass


x = D()
x.m()
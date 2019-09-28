class Example(object):
    pass
c = Example()
c.i = 5
print(c.i)

class Example(object):
    i = 0
    def __init__(self, i):
       self.i = i
    def display(self):
        print(i)
        pass
    pass
c = Example(5)
c.display()
c.i = 5
print(c.i)
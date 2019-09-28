class Test:
    def __init__(self):
        print("I am init")
        pass
    @staticmethod
    def sum(self,*args,**kwargs):
        print(type(args))
        print(kwargs)
        pass


Test.sum(10, 20, 30, 40,('a',10))

a = (i*2 for i in range(10))
for i in a:
    print(i)

print(range(10))
print(xrange(10))
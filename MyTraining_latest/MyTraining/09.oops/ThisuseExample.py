class Example(object):
    def __init__(self):
        print("I am default Constructor")
        pass
    def __init__(self,a):
        print("I am single parameter constructor")
        pass
    def __init__(self,a,b):
        print("I am base double parameter constructor")
        pass
    pass

e = Example()

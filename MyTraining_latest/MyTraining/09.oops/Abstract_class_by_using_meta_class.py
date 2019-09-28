from abc import ABCMeta, abstractmethod

class MyABC:
    __metaclass__ = ABCMeta

    @abstractmethod
    def sum(self):
        pass

class child(MyABC):
    def sum(self):
        print 9 + 9

    def display(self):
        print "display"
        pass


c = child()
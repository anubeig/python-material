#https://www.smartfile.com/blog/abstract-classes-in-python/

from abc import ABC,abstractmethod
class AbcExample01(ABC):
    @abstractmethod
    def execute(self):
        pass
class child(AbcExample01):
    def execute(self):
        print("Heloo")

c = child()
c.execute() # print Heloo

a = AbcExample01()   # give following error

"""
Traceback (most recent call last):
  File "main.py", line 13, in <module>
    a = AbcExample01()
TypeError: Can't instantiate abstract class AbcExample01 with abstract methods foo
"""

#Let’s try creating a concrete class, without implementing the execute method.

class AbcExample01(ABC):
    @abstractmethod
    def execute(self):
        pass
class ConcreteOperation(AbcExample01):
    pass

c = ConcreteOperation()
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class ConcreteOperation with abstract methods execute
"""

"""
In concrete class if we dont implement abstract method then we cant create object for that class.
We have to implement abstract method in child class(concrete class) otherwise we cannot create object of the child class.
"""

#multiple inheritance with abstratc class

from abc import ABC,abstractmethod
class AbcExample01(ABC):
    @abstractmethod
    def execute(self):
        pass
class ConcreteOperation(AbcExample01,ABC):
    pass

"""
class ConcreteOperation(ABC,AbcExample01):                                            # we cannot give ABC left of the class it throws the following error
    pass

sh-4.3$ python3 main.py
Traceback (most recent call last):
  File "main.py", line 6, in <module>
    class ConcreteOperation(ABC,AbcExample01):
  File "/usr/lib64/python3.4/abc.py", line 133, in __new__
    cls = super().__new__(mcls, name, bases, namespace)
TypeError: Cannot create a consistent method resolution
order (MRO) for bases AbcExample01, ABC
"""
class Demo(ConcreteOperation):
    def execute(self):
        print("Hello")
        pass
c = Demo()
c.execute()
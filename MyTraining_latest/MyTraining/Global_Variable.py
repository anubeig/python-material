z = 10
def afunction():
    global z
    print(1)
    pass
    print(z)
    z = 9


def afunction01():
    print(1)
    pass
    print(z)

afunction()
print(z)
afunction01()

"""
a = 10
def f():
  print(1)
  print(a) # UnboundLocalError raised here
  a = 20
f()
"""

def f():
    global z
    print(z)
    z=12
    print(z)
f()
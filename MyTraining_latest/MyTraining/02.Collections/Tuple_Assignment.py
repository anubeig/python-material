(a, b, c) = (1, 2, 3)

print a,b,c #1 2 3

#(a, b, c, d) = (1, 2, 3) # ValueError: need more than 3 values to unpack

def add(x, y):
    return x + y

print add(3, 4)
z = (5, 4)
print add(*z) # this line will cause the values to be unpacked
print add(z) # this line causes an error #def add(x, y):
    return x + y

print add(3, 4)
z = (5, 4)
print add(*z) # this line will cause the values to be unpacked
print add(z) # this line causes an error #TypeError: add() takes exactly 2 arguments (1 given)

"""
Once in a while, it is useful to swap the values of two variables.
With conventional assignment statements, we have to use a temporary variable.
For example, to swap a and b:

temp = a
a = b
b = temp
"""

#Tuple assignment solves this problem neatly:

(a, b) = (b, a)


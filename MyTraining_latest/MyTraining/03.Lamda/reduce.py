"""
The reduce is in the functools in Python 3.0. It is more complex.
It accepts an iterator to process, but it's not an iterator itself. It returns a single result:
"""

print reduce( (lambda x, y: x * y), [1, 2, 3, 4] )

"""
output:-
24
"""
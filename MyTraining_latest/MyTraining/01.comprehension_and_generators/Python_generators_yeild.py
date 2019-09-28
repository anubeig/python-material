#https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
#http://zetcode.com/lang/python/itergener/

def fun():
    result = 1 * 1
    yield result
    result = 2 * 2
    yield result
    result = 3 * 3
    yield result
    pass


for value in fun():
    print value

result = fun()
print next(result)
print next(result)
print next(result)

"""
print next(result) == this staetement gives the following error

Traceback (most recent call last):
  File "main.py", line 14, in <module>
    print next(result)
StopIteration

Because we are trying out of index(3)

"""
"""
sh-4.3$ python main.py
1
4
9
1
4
9
"""

"""
What's the magic part? Glad you asked! When a generator function calls yield,
the "state" of the generator function is frozen;
the values of all variables are saved and the next line of code to be executed is recorded until next() is called again.
Once it is, the generator function simply resumes where it left off. If next() is never called again,
the state recorded during the yield call is (eventually) discarded.
"""
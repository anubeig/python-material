"""
Fun With contextlib
Context managers are so useful, they have a whole Standard Library module devoted to them!
contextlib contains tools for creating and working with context managers.
One nice shortcut to creating a context manager from a class is to use the @contextmanager decorator.
To use it, decorate a generator function that calls yield exactly once.
Everything before the call to yield is considered the code for __enter__().
Everything after is the code for __exit__().
Let's rewrite our File context manager using the decorator approach:
"""
from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    print "open_file method is called"
    the_file = open(path, mode)
    print "Before yield statement"
    yield the_file
    print "After yield statement"
    the_file.close()

files = []

for x in range(2):
    with open_file('foo.txt', 'w') as infile:
        print "Started with block"
        files.append(infile)
        print "Ended with block"

for f in files:
    if not f.closed:
        print('not closed')

"""
sh-4.3$ python main.py
open_file method is called
Before yield statement
Started with block
Ended with block
After yield statement
open_file method is called
Before yield statement
Started with block
Ended with block
After yield statement

"""

"""
Description:-

As you can see, the implementation is considerably shorter. In fact, it's only five lines long! We open the file, yield it, then close it.
The code that follows is just proof that all of the files are, indeed, closed.
The fact that the program didn't crash is extra insurance it worked.
"""
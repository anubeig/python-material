#https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
"""
here are a number of ways to create a context manager.
The simplest is to define a class that contains two special methods: __enter__() and __exit__().
 __enter__() returns the resource to be managed (like a file object in the case of open()).
 __exit__() does any cleanup work and returns nothing.
"""

class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print "enter method is called"
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        print "exit method is called"
        self.open_file.close()

files = []
for _ in range(2):
    with File('foo.txt', 'w') as infile:
        print "Entered into with block"
        infile.write('foo')
        files.append(infile)
        print "End of with block"

"""
sh-4.3$ python main.py
enter method is called
Entered into with block
End of with block
exit method is called
enter method is called
Entered into with block
End of with block
exit method is called
"""

"""
Description:-
Let's go over what we have. Like any class, there's an __init__() method that
sets up the object (in our case, setting the file name to open and the mode to open it in).
 __enter__() opens and returns the file (also creating an attribute open_file so that we can refer to it in __exit__()).
  __exit__() just closes the file.
 Running the code above works because the file is being closed when it leaves the with File('foo.txt', 'w') as infile: block.
Even if code in that block raised an exception, the file would still be closed.
"""
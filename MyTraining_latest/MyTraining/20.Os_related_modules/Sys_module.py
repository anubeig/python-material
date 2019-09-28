#https://leemendelowitz.github.io/blog/how-does-python-find-packages.html
#http://ask.xmodulo.com/change-syspath-pythonpath-python.html

"""
When the Python interpreter executes a program which imports a module,
it examines all directory paths listed in sys.path until it finds the module.
By default, sys.path is constructed as a concatenation of
(1) the current working directory, (
2) content of PYTHONPATH environment variable, and
(3) a set of default paths supplied by the installed Python interpreter.

If the module you are trying to import is not found in any of the directories defined in sys.path,
you will encounter "Import Error: No module named XXXXX" error.
"""

import sys,os

print sys.path

# This won't work - there is no hi module
"""
import hi

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named hi
"""
# Create a hi module in your home directory.
home_dir = os.path.expanduser("~")
print home_dir
my_module_file = os.path.join(home_dir, "hi.py")
with open(my_module_file, 'w') as f:
  f.write('print "hi"\n')
  f.write('a=10\n')

# Add the home directory to sys.path
sys.path.append(home_dir)
print sys.path

# Now this works, and prints hi!
import hi
print hi.a

"""
sh-4.3$ python main.py
['/home/cg/root', '/usr/lib64/python27.zip', '/usr/lib64/python2.7', '/usr/lib64/python2.7/plat-linux2', '/usr/lib64/python2.7/lib-tk', '/usr/lib64/python2.7/lib-old', '/usr/li
b64/python2.7/lib-dynload', '/usr/lib64/python2.7/site-packages', '/usr/lib/python2.7/site-packages']
/home/cg/root
['/home/cg/root', '/usr/lib64/python27.zip', '/usr/lib64/python2.7', '/usr/lib64/python2.7/plat-linux2', '/usr/lib64/python2.7/lib-tk', '/usr/lib64/python2.7/lib-old', '/usr/li
b64/python2.7/lib-dynload', '/usr/lib64/python2.7/site-packages', '/usr/lib/python2.7/site-packages', '/home/cg/root']
hi
10
"""

r = range(10000)
print(sys.getsizeof(r))  # 80072

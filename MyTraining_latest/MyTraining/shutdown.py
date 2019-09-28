import atexit
import sys
import os

print("Starting Test Python Module");

def testmethod():
    print("From test method")

atexit.register(testmethod)

print("Terminating Test Python Module");

def sum():
    print "Sum"

sum()

"""
sh-4.3$ python main.py
Starting Test Python Module
Terminating Test Python Module
Sum
From test method



As you can notice it prints "From test method" at the end by executing registered method  testmethod.


Note :
Previously you could do the same by importing sys module and then using sys.exitfunc = testmethod but  sys.exitfunc is deprecated since python 2.4 and is removed since python 3.0.
The atexit module defines a single function to register cleanup functions. Functions thus registered are automatically executed upon normal interpreter termination.
atexit runs these functions in the reverse order in which they were registered; if you register A, B, and C, at interpreter termination time they will be run in the order C, B, A.
The functions registered via this module are not called when the program is killed by a signal not handled by Python, when a Python fatal internal error is detected, or when os._exit() is called.

"""

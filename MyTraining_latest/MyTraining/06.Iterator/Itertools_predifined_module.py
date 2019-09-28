#https://pymotw.com/2/itertools/
#http://programeveryday.com/post/using-python-itertools-to-save-memory/


from itertools import *

for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print(i)

"""
$ python itertools_chain.py

1
2
3
a
b
c

"""

#izip() returns an iterator that combines the elements of several iterators into tuples.
# It works like the built-in function zip(), except that it returns an iterator instead of a list.

from itertools import *

for i in zip([1, 2, 3], ['a', 'b', 'c']):
    print(i)

"""
$ python itertools_izip.py

(1, 'a')
(2, 'b')
"""


for i in range(5):
    print(i)
#https://code-maven.com/range-vs-xrange-in-python
import sys

r = range(10000)
print(sys.getsizeof(r))  # 80072

x = xrange(10000)
print(sys.getsizeof(x))  # 40

"""
The variable holding the range created by range uses 80072 bytes while the variable created by xrange only uses 40 bytes.

The reason is that range creates a list holding all the values while xrange creates an object that can iterate over the numbers on demand.
"""

print(type(r))    # <type 'list'>
print(type(x))    # <type 'xrange'>

"""
Speed - Benchmarking range and xrange

The "cost" of the memory saving is that looking up indexes in xrange will take slightly longer.
This benchmark code that uses the timeit module shows that the xrange version is 10% slower:
"""

import timeit

r = range(10000)
x = xrange(10000)


def range_index():
    z = r[9999]


def range_xindex():
    z = x[9999]


if __name__ == '__main__':
    import timeit

    print(timeit.timeit("range_index()", setup="from __main__ import range_index", number=10000000))
    print(timeit.timeit("range_xindex()", setup="from __main__ import range_xindex", number=10000000))

"""
OUTPut:-
sh-4.3$ python main.py
1.12523794174
1.22963786125
"""
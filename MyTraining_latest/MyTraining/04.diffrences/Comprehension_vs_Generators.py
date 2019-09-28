#https://code-maven.com/list-comprehension-vs-generator-expression

"""
A Generator Expression is doing basically the same thing as a List Comprehension does, but the GE does it lazily.
The difference is quite similar to the difference between range and xrange.

A List Comprehension, just like the plain range function, executes immediately and returns a list.

A Generator Expression, just like xrange returns and object that can be iterated over.

The comparision is not perfect though, because in an object returned by the generator expression, we cannot access an element by index.

The difference between the two kinds of expressions is that the List comprehension is enclosed in square brackets []
while the Generator expression is enclosed in plain parentheses ().
"""

print sum([x * x for x in range(1, 10)])
print sum(x * x for x in range(1, 10))

import sysyugtuk

l = [n * 2 for n in range(10)]  # List comprehension
g = (n * 2 for n in range(10))  # Generator expression

print(type(l))  # <type 'list'>
print(type(g))  # <type 'generator'>

print(sys.getsizeof(l))  # 9032
print(sys.getsizeof(g))  # 80

print l  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print g  # <generator object <genexpr> at 0x7f0be47dd7d0>

print(l[4])  # 8
# print(g[4])   # TypeError: 'generator' object has no attribute '__getitem__'

for v in l:
    print v
    pass
for v in g:
    print v
    pass
"""
Generators are iterators, but you can only iterate over them once.
It’s because they do not store all the values in memory, they generate the values on the fly:
"""
print(sys.getsizeof(g)) # 80
for v in g:
    print "2nd time"                        # it wont print any values bcoz generator iterate only once
    print v
    pass

"""
output:-
sh-4.3$ python main.py
285
285
<type 'list'>
<type 'generator'>
200
80
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
<generator object <genexpr> at 0x7f0be47dd7d0>
8
0
2
4
6
8
10
12
14
16
18
0
2
4
6
8
10
12
14
16
18
"""
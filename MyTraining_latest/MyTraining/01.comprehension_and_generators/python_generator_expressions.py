"""
Generator Expressions

In Python, generators provide a convenient way to implement the iterator protocol.
Generator is an iterable created using a function with a yield statement.
The main feature of generator is evaluating the elements on demand.
When you call a normal function with a return statement the function is terminated whenever it encounters
a return statement. In a function with a yield statement the state of the function is
“saved” from the last call and can be picked up the next time you call a generator function.

Generator expression allows creating a generator on a fly without a yield keyword.
However, it doesn’t share the whole power of generator created with a yield function.
 The syntax and concept is similar to list comprehensions:

>>> gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
>>> for x in gen_exp:
...     print(x)
0
4
16
36
64
In terms of syntax, the only difference is that you use parenthesis instead of square brackets.
 However, the type of data returned by list comprehensions and generator expressions differs.

>>> list_comp = [x ** 2 for x in range(10) if x % 2 == 0]
>>> gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
>>> print(list_comp)
[0, 4, 16, 36, 64]
>>> print(gen_exp)
<generator object <genexpr> at 0x7f600131c410>
The main advantage of generator over a list is that it take much less memory.

We can check how much memory is taken by both types using sys.getsizeof() method.

Note: in Python 2 using range() function can't actually reflect the advantage in term of size,
as it still keeps the whole list of elements in memory. In Python 3, however,
this example is viable as the range() returns a range object.

>>> from sys import getsizeof
>>> my_comp = [x * 5 for x in range(1000)]
>>> my_gen = (x * 5 for x in range(1000))
>>> getsizeof(my_comp)
9024
>>> getsizeof(my_gen)
88
Generator yields one item at a time thus it is more memory efficient compared to the list.
For example, when you want to iterate over a list, python reserves memory for the whole list.
Generator won’t keep the whole sequence in memory and will only “generate” the next element of the sequence on demand.
"""
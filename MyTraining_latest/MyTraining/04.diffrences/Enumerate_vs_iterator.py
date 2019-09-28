"""
enumerate() is one of the built-in Python functions. It returns an enumerate object.
In our case that object is a list of tuples (immutable lists), each containing a pair of count/index and value.
"""

choices = ['pizza', 'pasta', 'salad', 'nachos']

list1 = enumerate(choices)

print(list(list1))

for index, value in enumerate(choices):
    print(index, value)

print(type(list1))

# We may easily change the start count/index with help of enumerate(sequence, start=0)

for index, value in enumerate(choices, start=5):
    print(index, value)

"""
output:-

sh-4.3$ python3 main.py
[(0, 'pizza'), (1, 'pasta'), (2, 'salad'), (3, 'nachos')]
0 pizza
1 pasta
2 salad
3 nachos
<class 'enumerate'>
5 pizza
6 pasta
7 salad
8 nachos

"""

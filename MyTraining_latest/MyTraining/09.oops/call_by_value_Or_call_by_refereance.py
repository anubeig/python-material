def foo(bar):
    bar.append(42)
    print(bar)
    # >> [42]

answer_list = []
foo(answer_list)
print(answer_list)

def foo(bar):
    bar = 'new value'
    print (bar)
    # >> 'new value'

answer_list = 'old value'
foo(answer_list)
print(answer_list)

def foo(bar):
    tup1 = (42)
    bar = tup1
    print(bar)
    # >> [42]

answer_list = ()
foo(answer_list)
print(answer_list)

some_guy = 'Fred'

first_names = []
first_names.append(some_guy)

another_list_of_names = first_names
another_list_of_names.append('George')
some_guy = 'Bill'

print (some_guy, first_names, another_list_of_names)

"""
sh-4.3$ python main.py
[42]
[42]
42
()
new value
old value
('Bill', ['Fred', 'George'], ['Fred', 'George'])
"""
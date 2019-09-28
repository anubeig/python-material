table = [0] * 10  # our Hash table
print table

def hash_function(x):  # Our hash function
    return x % 10

def insert(table, input, value):  # inserting data into hashtable
    table[hash_function(input)] = value

insert(table, 41, 'apple')
insert(table, 93, 'banana')
print table
"""
[0, 'apple', 0, 'tangerine', 0, 0, 0, 0, 0, 0]
"""

insert(table, 13, 'tangerine')  # here collision occurs we lost 'banana'
print table
"""[0, 'apple', 0, 'tangerine', 0, 0, 0, 0, 0, 0] """

"""
There are several ways to resolve collisions, such as chaining (we are going to use this), open addressing and so on.

Second Approach with chaining

Now, instead of only a list as an output table, we use a list of lists.
Every list inside this master list is a sort of a bucket in which we insert (key,value) pairs.

"""

table = [[] for x in range(10)]
print table


def insert(table, input, value):
    table[hash_function(input)].append((input, value))


insert(table, 41, 'apple')
insert(table, 93, 'banana')
insert(table, 13, 'tangerine')  # linked list with channing is using here so value doesnt lost like above
print table

"""[[], [(41, 'apple')], [], [(93, 'banana'), (13, 'tangerine')], [], [], [], [], [], []]"""
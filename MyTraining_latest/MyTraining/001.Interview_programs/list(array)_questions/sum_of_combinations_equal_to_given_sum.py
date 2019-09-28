"""
I have a list of numbers, e.g.

numbers = [1, 2, 3, 7, 7, 9, 10]
As you can see, numbers may appear more than once in this list.

I need to get all combinations of these numbers that have a given sum, e.g. 10.

The items in the combinations may not be repeated, but each item in numbers has to be treated uniquely, that means e.g. the two 7 in the list represent different items with the same value.

The order is unimportant, so that [1, 9] and [9, 1] are the same combination.

There are no length restrictions for the combinations, [10] is as valid as [1, 2, 7].

How can I create a list of all combinations meeting the criteria above?

In this example, it would be [[1,2,7], [1,2,7], [1,9], [3,7], [3,7], [10]]

"""

import itertools
numbers = [1, 2, 3, 7, 7, 9, 10]
result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == 10]
print result



import itertools
list = [1, 1, 2, 3, 4, 5,]
uniquelist = set(list)
targetsum = 5
for n in itertools.combinations(uniquelist, 2):
    if n[0] + n[1] == targetsum:
        print str(n[0]) + " + " + str(n[1])

"""
sh-4.4$ python main.py
(1, 2)
(1, 3)
(1, 4)
1 + 4
(1, 5)
(2, 3)
2 + 3
(2, 4)
(2, 5)
(3, 4)
(3, 5)
(4, 5)
"""
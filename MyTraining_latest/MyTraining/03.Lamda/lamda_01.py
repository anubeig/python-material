"""
The lambda operator or lambda function is a way to create small anonymous functions,
 i.e. functions without a name.
These functions are throw-away functions, i.e. they are just needed where they have been created

The general syntax of a lambda function is quite simple:
lambda argument_list: expression The general syntax of a lambda function is quite simple:
lambda argument_list: expression
"""

f = lambda x,y:x+y

print f(7,8)

"""
output:-
15
"""
#finding the length of words in a sentence

sentences = 'It is raining in India'

words = sentences.split()

lengths = map(lambda w:len(w), words)

print lengths

import math
square_root = lambda x: math.sqrt(x)

"""
Things get more interesting when you use + and * to specify repetition in the pattern

+ -- 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
* -- 0 or more occurrences of the pattern to its left
? -- match 0 or 1 occurrences of the pattern to its left
Leftmost & Largest

First the search finds the leftmost match for the pattern,
and second it tries to use up as much of the string as possible -- i.e. + and * go as far as possible
(the + and * are said to be "greedy").
"""
import re
## i+ = one or more i's, as many as possible.
match = re.search(r'pi+', 'piiig')
if match:
    print match.group()
else:
    print "Not Found"

## \s* = zero or more whitespace chars

match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
if match:
    print match.group()
else:
    print "Not Found"

match = re.search(r'\d\s*\d\s*\d', 'xx123xx')
if match:
    print match.group()
else:
    print "Not Found"
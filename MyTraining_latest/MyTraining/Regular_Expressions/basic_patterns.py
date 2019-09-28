#https://developers.google.com/edu/python/regular-expressions
import re

#find the pattern start word with Anu

str1 = "Anubaig"
match = re.search(r'^Anu\w+',str1)
print match.group()

str2 = 'Anumogal'
match = re.search(r'^Anu\w+',str2)
print match.group()

str2 = 'numogal'
match = re.search(r'^Anu\w+',str2)
if match:
    print match.group()
else:
    print "Not Found"

#Find the patter end with baig


## . = any char but \n
match = re.search(r'..g', 'piiig')
if match:
    print match.group()
else:
    print "Not Found"

## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g')
if match:
    print match.group()
else:
    print "Not Found"

match = re.search(r'\w\w\w', '@@abcd!!')
if match:
    print match.group()
else:
    print "Not Found"

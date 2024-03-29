"""
findall() is probably the single most powerful function in the re module.
Above we used re.search() to find the first match for a pattern.
findall() finds *all* the matches and returns them as a list of strings, with each string representing one match.
"""

import re
## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)
for email in emails:
    print email

"""
findall With Files

For files, you may be in the habit of writing a loop to iterate over the lines of the file, 
and you could then call findall() on each line. Instead, let findall() do the iteration for you -- much better! 
Just feed the whole file text into findall() and let it return a list of all the matches in a single step
 (recall that f.read() returns the whole text of a file in a single string):
"""

# Open file
f = open('test.txt', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'some pattern', f.read())
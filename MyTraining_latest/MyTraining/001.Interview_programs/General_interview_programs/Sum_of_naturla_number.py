#Sum of natural number
"""
n*(n+1)/2
For example, if n = 16, the sum would be (16*17)/2 = 136.
"""

n = 16

sum = (n*(n+1))/2
print sum #136

#using Recursion

def recur_sum(n):
   """Function to return the sum
   of natural numbers using recursion"""
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)
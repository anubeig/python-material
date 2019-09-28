"""
The other respondents are correct in describing the double leading and trailing underscores as a
naming convention for "special" or "magic" methods.

While you can call these methods directly ([10, 20].__len__() for example),
the presence of the underscores is a hint that these methods are intended to be invoked indirectly (len([10, 20])
for example).
 Most python operators have an associated "magic" method
 (for example, a[x] is the usual way of invoking a.__getitem__(x)).
"""
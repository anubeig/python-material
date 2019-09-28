str1 = "Anu baig"

print('%s'%(str1))

print('%r'%(str1))

#print('%d'%(str1)) TypeError: %d format: a number is required, not str

str1 = "Anu baig"

print(type('%s'%(str1)))

print(type('%r'%(str1)))

str2 = 123

print('%d'%(str2))

"""
sh-4.3$ python3 main.py
Anu baig
'Anu baig'
<class 'str'>
<class 'str'>
123
"""
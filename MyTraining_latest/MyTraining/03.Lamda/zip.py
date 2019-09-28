
#zip function takes two equal-length collections, and merges them together in pairs.

a = [1, 2, 3, 4, 5]
b = [2, 2, 9, 0, 9]

print(a+b)  # adding without zip
for value in zip(a, b): # with zip
    print(value)
    print(type(value))

list1 = [1,2,3,4,5]
list2 = ['anu','baig']

print(list1+list2)
zipped = zip(list1,list2) io[]\4/*= oo-4.3$ py///////////////89+.py
[1, 2, 3, 4, 5, 2, 2, 9, 0, 9]
(1, 2)
<class 'tuple'>
(2, 2)
<class 'tuple'>
(3, 9)
<class 'tuple'>
(4, 0)
<class 'tuple'>
(5, 9)
<class 'tuple'>
[1, 2, 3, 4, 5, 'anu', 'baig']
<zip object at 0x7f01fa747548>
(1, 'anu')
(2, 'baig')

print(zipped)

for i in zipped:
    print(i)
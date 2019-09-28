n=10
a=0
b=1
for i in range(1,n):
    print(b)
    c=a+b
    a=b
    b=c

list = []
list.append(3)
list.append(5)
print(list)
print(list.remove(3))
print(list)

dict1 = {'name':'Anu'}

dict1['age'] = 10
print(dict1)
del dict1['name']
print(dict1)
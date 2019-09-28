class emp:
    id ,name = ''
    def __init__(self,id,name):
        self.id,self.name = id,name
        pass

e1 = emp(10,'Anu')
e2 = emp(20,'baig')
e3 = emp(30,'mogal')

employees = [e2 , e1, e3]

print("Before sorting")
for i in range(0,len(employees)):
    print(employees[i].id,employees[i].name)

import operator
employees.sort(key=operator.attrgetter("id","name"), reverse=False)

print("After sorting")
print("Before sorting")
for i in range(0,len(employees)):
    print(employees[i].id,employees[i].name)

"""
Before sorting
(20, 'baig')
(10, 'Anu')
(30, 'mogal')

After sorting
(10, 'Anu')
(20, 'baig')
(30, 'mogal')
"""
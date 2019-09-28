import pandas as pn
dict1 = {'Names':['Nazeer','Malika','Anu','Parru','Arshiya','Seema','Amir','Asma','Mateen','Ashiq'],
         'Age':[55,48,30,29,25,22,7,3,1,1],
         'food':['Chicken','Fish','Chicken','Mutton','Ice','Ice','Fish','Mutton','ceralac','cerelac'],
         'weight':[70,55,71,45,44,43,15,9,7,4]}
df = pn.DataFrame(dict1);

"sorting"
print(df.sort_values('Names'))
print(df.sort_values('Names',ascending=False))
print(df.sort_values(['Names','Age'],ascending=[False,True]))

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pn.DataFrame(ipl_data)

"groupby"
print(df.groupby('Team').groups)
"Multiple columns"
print(df.groupby((['Team','Year'])).groups)
print("get_group method")
print(df.groupby('Year').get_group(2014))

"Iterating throup groupby object"
for group,name in df.groupby('Team'):
    print(group)
    print(name)

import numpy as np
"Aggregate function"
print(df.groupby('Year').agg(np.mean))



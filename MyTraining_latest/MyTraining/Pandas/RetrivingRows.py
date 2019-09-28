"""
To print a specific row we have couple of pandas method

loc - It only get label i.e column name or Features
iloc - Here i stands for integer, actually row number
ix - It is a mix of label as well as integer
How to use for specific row

loc
df.loc[row,column]
For first row and all column

df.loc[0,:]
For first row and some specific column

df.loc[0,'column_name']
iloc
For first row and all column

df.iloc[0,:]
For first row and some specific column i.e first three cols

df.iloc[0,0:3]
"""

import pandas as pn
dict1 = {'Names':['Nazeer','Malika','Anu','Parru','Arshiya','Seema','Amir','Asma','Mateen','Ashiq'],
         'Age':[55,48,30,29,25,22,7,3,1,1],
         'food':['Dal','Fish','Chicken','Mutton','sheek','Ice','Maggi','gosh','ceralac','pro'],
         'weight':[70,55,71,45,44,43,15,9,7,4]}
df = pn.DataFrame(dict1);


print(type(df.loc[1,]))

"First Row by loc method"
print(df.loc[1,])

"First Row and First Column"
print(df.loc[1,'Age'])

"third row by iloc method"
print(df.iloc[3])



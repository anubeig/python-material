import pandas as pn

dict1 = {'Names':['Nazeer','Malika','Anu','Parru','Arshiya','Seema','Amir','Asma','Mateen','Ashiq'],
         'Age':[55,48,30,29,25,22,7,3,1,1],
         'food':['Dal','Fish','Chicken','Mutton','sheek','Ice','Maggi','gosh','ceralac','pro'],
         'weight':[70,55,71,45,44,43,15,9,7,4]}
df = pn.DataFrame(dict1);

"Print the whole data"

print(df)

"Print the sample data"

print(df.head())
print(df.tail())
"Random Lines"
print(df.sample(2))

"Specify columns"
print(df['Age'])
print(df[['Age','food']])

"Filtering data"
print("Filtering data")
print(df[df.Age >= 5])
#print(df[df.Names.like("Anu")])

print(df.query('Age > 30'))




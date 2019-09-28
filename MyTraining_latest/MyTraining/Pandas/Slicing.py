import pandas as pn
dict1 = {'Names':['Nazeer','Malika','Anu','Parru','Arshiya','Seema','Amir','Asma','Mateen','Ashiq'],
         'Age':[55,48,30,29,25,22,7,3,1,1],
         'food':['Dal','Fish','Chicken','Mutton','sheek','Ice','Maggi','gosh','ceralac','pro'],
         'weight':[70,55,71,45,44,43,15,9,7,4]}
df = pn.DataFrame(dict1);

print(df);

"print(df[0]) gives keyerror in pandas we cannot retrive values by index"

print(df['Names']);
print(df['food']);
print(df[:2]);

print(df[1:4])

print(df[2:])
#reverse order
print(df[::-1])

print(df[1:2])
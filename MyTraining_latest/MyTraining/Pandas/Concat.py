import pandas as np

df1 = np.DataFrame({'name':['A','B','C'],'age':[10,20,30]})
df2 = np.DataFrame({'name':['D','E'],'age':[40,50]}, index=[4,5])

df3 = np.concat([df1,df2])
print(df3)

print(df3.values[0])
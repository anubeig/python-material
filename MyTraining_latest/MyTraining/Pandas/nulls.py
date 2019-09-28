import pandas as pd

df = pd.DataFrame({'Last_Name': ['Smith', None, 'Brown'],
                   'First_Name': ['John', 'Mike', 'Bill'],
                   'Age': [35, 45, None]})

print(df[pd.notnull(df['Last_Name'])])
print(df[pd.isnull(df['Age'])])

print(df.dropna())

#from pandas import DataFrame
import pandas as pn
Employees = {'Name of Employee': ['Jon','Mark','Tina','Maria','Bill','Jon','Mark','Tina','Maria','Bill','Jon','Mark','Tina','Maria','Bill','Jon','Mark','Tina','Maria','Bill'],
             'Sales': [1000,300,400,500,800,1000,500,700,50,60,1000,900,750,200,300,1000,900,250,750,50],
             'Quarter': [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4],
             'Country': ['US','Japan','Brazil','UK','US','Brazil','Japan','Brazil','US','US','US','Japan','Brazil','UK','Brazil','Japan','Japan','Brazil','UK','US']
            }

df = pn.DataFrame(Employees, columns= ['Name of Employee', 'Sales','Quarter','Country'])

print(df)

"""
Let’s say that your goal is to determine the:

Total sales per employee
Total sales by country
Sales by both employee and country
Max individual sale by country
Mean, median and min sales by country
"""

#Total sales per employee
print(df.pivot_table(index=['Name of Employee'], values=['Sales'],aggfunc='sum'))

#Total sales by country
print(df.pivot_table(index=['Country'],values=['Sales'],aggfunc='sum'))

#Sales by both employee and country
print(df.pivot_table(index=['Name of Employee','Country'],values=['Sales'],aggfunc='sum'))

print(df.pivot_table(index=['Country'],values=['Sales'],aggfunc='max'))

print(df.pivot_table(index=['Country'],values=['Sales'],aggfunc=['sum','max','min','mean','median']))


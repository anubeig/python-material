import pandas as pd
import numpy as np

# Create a DataFrame
d = {
    'Name': ['Alisa', 'Bobby', 'Cathrine', 'Alisa', 'Bobby', 'Cathrine',
             'Alisa', 'Bobby', 'Cathrine', 'Alisa', 'Bobby', 'Cathrine'],
    'Exam': ['Semester 1', 'Semester 1', 'Semester 1', 'Semester 1', 'Semester 1', 'Semester 1',
             'Semester 2', 'Semester 2', 'Semester 2', 'Semester 2', 'Semester 2', 'Semester 2'],

    'Subject': ['Mathematics', 'Mathematics', 'Mathematics', 'Science', 'Science', 'Science',
                'Mathematics', 'Mathematics', 'Mathematics', 'Science', 'Science', 'Science'],
    'Result': ['Pass', 'Pass', 'Fail', 'Pass', 'Fail', 'Pass', 'Pass', 'Fail', 'Fail', 'Pass', 'Pass', 'Fail']}

df = pd.DataFrame(d, columns=['Name', 'Exam', 'Subject', 'Result'])
print(df)

print(pd.crosstab(df.Subject,df.Result))
print(pd.crosstab(df.Subject,df.Result,margins=True))
"margin=True displays the row wise and column wise sum of the cross table"

"We will calculate the cross table of subject, Exam and result as shown below"
print(pd.crosstab([df.Subject, df.Exam],df.Result, margins=True))
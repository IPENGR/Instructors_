#Removing Duplicates- Duplicate rows are rows that have been registered more than one time.

import pandas as pd
df = pd.read_csv('data2.csv')
print(df.duplicated()) #Returns True for every row that is a duplicate, otherwise False
df.drop_duplicates(inplace = True)  #To remove duplicates, use the drop_duplicates() method
print(df.to_string())



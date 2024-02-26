#pandas-Data Correlations

import pandas as pd
df = pd.read_csv('data2.csv')
print(df.corr())  #The corr() method calculates the relationship between each column in your data set.




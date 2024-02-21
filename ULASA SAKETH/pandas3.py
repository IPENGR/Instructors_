#DATA FRAMES
#Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
'''import pandas as pd
data={
    'topics':['java','javascript','python'],
    'classes':[2,1,1]
}
df=pd.DataFrame(data)
print(df)
#locate row
print(df.loc[0])  #loc attribute is used to return one or more specified row(s)
'''

#Named index

import pandas as pd
data={
    'cars': ['honda','audi','bmw'],
    'passing' : [2,1,3]
}
df=pd.DataFrame(data, index=['day1','day2','day3'])
print(df)
print(df.loc['day1'])  #locate named index
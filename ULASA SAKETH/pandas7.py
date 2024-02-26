#Fixing Wrong Data
#"Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".

import pandas as pd
df = pd.read_csv('data2.csv')
df.loc[7,'Duration'] = 45      #the value should be "45" instead of "450"
print(df.to_string())

#another way is removing rows
'''for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

#remember to include the 'inplace = True' argument to make the changes in the original DataFrame object instead of returning a copy

print(df.to_string())'''



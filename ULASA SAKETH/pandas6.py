#Data Cleaning:
#Empty Cells- Empty cells can potentially give you a wrong result when you analyze data.
#Return a new Data Frame with no empty cells
import pandas as pd
df = pd.read_csv('data2.csv')
new_df = df.dropna()  #the dropna() method returns a new DataFrame, and will not change the original.
print(new_df.to_string())
#Remove all rows with NULL values
df.dropna(inplace = True)  #it will remove all rows containing NULL values from the original DataFrame.
print(df.to_string())
#Replace NULL values with the number 130
df.fillna(130, inplace = True) #The fillna() method allows us to replace empty cells with a value
print(df.to_string())
df["Calories"].fillna(130, inplace = True)  #Replace NULL values in the "Calories" columns with the number 130
print(df.to_string())
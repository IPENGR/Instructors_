#pandas series
#A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type.

import pandas as pd
# Create a list 'a' containing integer values.
a=[1,2,3,4]
# Create a pandas Series 'b' from the list 'a'.
b=pd.Series(a)
print(b)
print(b[0])    #to find the index(values are labeled with their index number)


c=[2,6,8]
d=pd.Series(c,index = ['x','y','z'])    #creating own labels for values
print(d)
print(d[0])

#key value objects
e={'day1':10,'day2':20,'day3':30}    #key value pairs
f=pd.Series(e)
print(f)
#to select only some of the items in the dictionary, use the index
g={"day5":1,"day6":2,"day7":3}
h=pd.Series(g, index=["day5","day7"])
print(h)

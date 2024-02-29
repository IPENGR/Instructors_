#practice sets

import numpy as np

omg = set(np.arange(10))
print(type(omg))           # to know, what type 
print(omg)

a=set(np.arange(0,10,2))      
print(a)

b=set(np.arange(0,10,3))
print(b)

print(a.union(b))    #it will print all the elements in both sets as a single set without repeating elements

print(a.intersection(b))  # it will print the common elements from both sets as a single set

b.add(8)   #adding an element to the b set
print(b)

print(a.intersection(b))
print(a.difference(b))  #the elements in a - the elements in b

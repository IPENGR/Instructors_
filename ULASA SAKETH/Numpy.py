'''
NumPy is a Python library used for working with arrays.
'''
   
import numpy
import numpy as np

'''
a=np.array([1,2,3,4,5])
print(a)                  
print(a.ndim)           #dimensions
'''

b=np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(b)
print(b.ndim)           #dimensions
print(b.shape)          #it shows rows and columns
print(b.itemsize)       #in array the item size is 4
print(b.nbytes)         #10x4=40 

#accessing the array
print(b[1,2])           #(r,c) it will access the item
b=np.zeros((2,3))       #(r,c) it will give all zeros 
print(b)
b=np.ones((3,4))        #(r,c) it will give all ones
print(b)
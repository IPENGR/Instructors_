
'''Indexing in NumPy arrays is similar to indexing in Python lists, but NumPy provides additional capabilities for multidimensional arrays and advanced indexing techniques. Here's an overview of indexing in NumPy arrays:

Basic Indexing:

You can use square brackets [] to access individual elements of a NumPy array by specifying the indices along each dimension.
Example:'''


import numpy as np
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])
print("arr  : -" , arr)
print(arr[:,1])
print(arr[2,:])




aarr=np.array(['apple','banana','mouse'])
print("aarr :",aarr,aarr[1,]) 
print(arr[0, 0])  # Output: 1 (element at row 0, column 0)
print(arr[1, 2]) # Output: 6 (element at row 1, column 2)
a=np.arange(10).reshape((2,5))
print(a)
print(a[:,::-1])   

#Slicing:

#NumPy arrays support slicing along each dimension, allowing you to extract subarrays or specific ranges of elements.
#Example:
#1 DIMENSIONAL ARRAY
a1=np.array([1,2,3,4,5,6,7,8])
print(a1)
print(a1[::-1])
print(a1[1::2])
print(a1[-1:-5:-1])


#2 DIMENSIONAL ARRAY
print("from 2 d arrays")
arr = np.array([[1, 2, 3],
                [4, 5, 6], 
                [7, 8, 9],
                [10, 11, 12]])
print(arr.ndim)

print(arr[1,])

print(arr[1:3,1:3])
print(arr[0:2, 1:])  # Output: [[2 3]


#iterating through the array using for loop
a=np.array([1,2,3,4,5,5,6,6])
for i in a:
    print (i)
# itirating for 2d array
b=np.array([[1,2,3],[4,5,6],[7,8,9]])


for x in b:
  print("X represents 1 d array")
  print("x :",x)
  for y in x:
    print(y)




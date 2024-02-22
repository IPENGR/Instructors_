'''
numpy  :- 
NumPy is a powerful library in Python for numerical computing. It provides support for multidimensional arrays and matrices, 
along with a collection of mathematical functions to operate on these arrays efficiently. 
Here's a brief overview of NumPy's capabilities:

1)Arrays: NumPy's main object is the homogeneous multidimensional array (numpy.ndarray). 
It is a table of elements, all of the same type, indexed by a tuple of non-negative integers.




'''
import  numpy as np
# Creating an Array
lst=[1,2.2,'30',3,4,5] # List can contain different data types
print(lst)
arr1=np.array(lst,dtype='str') # Creating an array from a list, specifying the data type
print(arr1)

#two dimensional array creating 
lst1=[[3,4],[1,2]]
arr2=np.array([[2,4,6,8],['s',6,9,4]])
print(arr2)
arr3=np.arange(1,9)
print(arr3)


arr4=np.arange(2,10).reshape((2,4))#Creating an array with range values 2d array


print(arr4)
print(type(arr3))
print("hello numpy")
arr5=np.zeros((3,3),int) #creates and returns a new array of given shape and type, filled with zeros.
print(arr5)
arr6=np.ones((6,2),dtype=int)
print(arr6)

#ndim(ndarray) returns the number of dimensions of the array.
print(arr6.ndim)
print(arr2.ndim)
print(arr4.ndim)
arr7=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]] #A three dimensional array
arr8=np.array(arr7)
print(arr8)
s=np.where(arr8==9)



#1) shape 
 #NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
import numpy as np

arr = np.array([[1, 2, 3, 4], 
                [5, 6, 7, 8],
                [9, 2, 3, 4]])

print("shape of the arr",arr.shape)

#to change the shape of an arraty we use  reshape() method
new_arr=arr.reshape(2,6) # it will give error if
print(new_arr)

#reshaping the 1d to 3d

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)

a=np.array_split(arr,3)
print(a)
print(a[1])


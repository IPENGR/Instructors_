#Create an array with data type string:

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)




arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

#Change data type from integer to boolean:



arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)





#coying the data of an array by using copy() in numpy
arr=np.array([1,2,3,4,5])


arr1=arr.copy()
arr[1]=32
print("arr :",arr)

print("arr1 :",arr1)

#creating a view using view()

arr2=arr.view()
arr[2]=321
arr2[1]=6789
print("arr2 :",arr2)
print("again arr :",arr)


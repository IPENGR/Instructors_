#joining of two arrays

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a,b)
c = np.concatenate((a, b))  # Join along axis 0 by default
print(f"Array c after joining a and b:\n{c}\n")

# joining two dimensional array
d = np.array([[7,8],[9,10]])
e = np.array([[11,12], [13,14]])
f = np.concatenate((d, e),axis=0)

print(" f joining  d and e vertically:\n", f,"\n")

g = np.concatenate((d, e),axis=1)   
print(" g joining  d and e horizontal :\n", g,"\n")


#stack :-Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
#We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])
print(arr1)
print(arr2)

arr = np.stack((arr1, arr2), axis=1)

print("output of stak method :",arr)

#numPy provides a helper function: hstack() to stack along rows.axis=0
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print("out from  hstack method \n ",arr)

#vstack(): NumPy provides a helper function: vstack()  to stack along columns..axis=1

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2)) 

print("output  from vstack method \n ",arr)

#NumPy provides a helper function: dstack() to stack along height, which is the same as depth in case of 3D arrays.
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print("output from  dstack method:\n",arr)



arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)

a=np.array_split(arr,3)
print(a)
print(a[1])



#search in the array
arr8=np.array([1,2,3,4,5,6,7,8,9,8,8,10])
s=np.where(arr8==8) #returns index of element which is equal to 9
print(s)



x = np.where(arr8%2 == 0)

print(x)


#searchsorted
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='left')

print(x)




arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)


#filtering the array


arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []


for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

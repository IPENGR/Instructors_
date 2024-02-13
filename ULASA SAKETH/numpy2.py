#three deminsional
import numpy
import numpy as np

a=np.array([[[1,2],[2,3],[3,4],[4,5]]])
print(a)
print(a.ndim)                #to know the dimensions
d=np.full((2,3),90)        #by giving r&c with a number,the matrix will fill with that number only
print(d)
s=np.random.rand(3,2)   #if we give some r&c, the matrix will be created with random numbers
print(s)
k=np.identity(5)        #the middle cross line will be 1 ,it will form 5*5 matrix
print(k)

#copy function
a=np.array([1,2,3,4])
b=a.copy()              #by giving copy func,there is no change in b
a[0]=10
print(a)
print(b)

#mathematical operations
k=np.array([1,2,3,4,5])
print(k+1)           #addition of an array
print(k-1)         #substraction of an array
print(k**2)    #power of a number in array
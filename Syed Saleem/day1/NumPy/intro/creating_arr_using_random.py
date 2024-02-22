import numpy as np

"""#rand()

a=np.random.rand(6)# generates values between 0 and 1  for an array of size 6
print( a)

a1=np.random.rand(3,5)
print()
print(a1)

#randn()

a=np.random.randn(4)
print()
print(a)
a=np.random.randn(2,4)
print(a)
"""

#randint()
a=np.random.randint(2,40,4)
print(a)
print(type(a))

#arthematic functions in numpy

arr=np.random.randint(2,9,10)
print(arr)
print()  
print("min value ::",np.min(arr),np.argmin(arr))
print()
print("max value ::",np.max(arr),np.argmax(arr))


a=np.array([[1,2,3],[6,7,3]])
print(a)
print("min in each row  ",np.min(a,axis=1) )
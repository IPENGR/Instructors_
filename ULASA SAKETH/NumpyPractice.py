import numpy as np
from numpy import random

x=random.randint(100)   #it Generates a random integer from 0 to 100
print(x)
y=random.rand()     #it Generates a random float from 0 to 1
print(y)
z=random.randint(100, size=(5))    #it Generates a 1-D array containing 5 random integers from 0 to 100
print(z)
a=random.randint(100, size=(3, 5))  #it Generates a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100
print(a)
b= random.rand(5) #it Generates a 1-D array containing 5 random floats
print(b)

#shuffling Arrays
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)    #changing arrangement of elements 
print(arr)

#normal distribution(Gaussian Distribution)
#it use the random.normal() method to get a Normal Data Distribution.
x=random.normal(size=(2, 3))
print(x)

x = random.exponential(scale=2, size=(2, 3))   #Generates a 2x3 array of random numbers from an exponential distribution with a scale of 2.
print(x)
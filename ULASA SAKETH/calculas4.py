#Eulers number:there is a special number that shows up quite a  bit in math called Euler's number 'e'
#it is same like a pi and is approximately 2.718

from math import *

x=3
result1=exp(x)  #exponential
result2=log(x)  #logarithmic
print(result1)
print(result2)

#plot
from sympy import *

x=symbols('x')
f=exp(x)
plot(f)
d=log(x)
plot(d)
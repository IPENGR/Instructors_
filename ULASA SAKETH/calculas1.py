#number sytem - natural numbers
#Eg:0,1,2,3,4....
for i in range(100):
    print(i)

#integers : Eg- z=...-3,-2,-1,0,1,2,3...

for i in range(-100,101):
    print(i)

#rational number : Eg-1/2
    
from sympy import *
a=Rational(3/2)
b=Rational(5/4)
c=a+b
print(c)

#irratiional number: It have an infinite number of decimals places with no clear pattern.

x=pi**2/pi**3 # pi=22/7=3.14
print(x)

#Real numbers: it includes rational and irrational numbers

n=[-2,0.34,27/12,10]
for i in n:
    print(i)

#Complex and Imaginary number = when you take the square root of a negative number,you end up with a
#complex/imaginary number

print(sqrt(-4))  # imaginary number are often denoted by i




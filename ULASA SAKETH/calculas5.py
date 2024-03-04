#limits: the way we express a value that is foreever being approached,but never reached,is through a limit
# lim 1/x = 0
#  x--oo


from sympy import *

x=symbols('x')
f= 1/x
result1=limit(f,x,oo)
print(result1)


#limits-euler's number 
#e=lim(1+1/x)**x
#   x--oo
n=symbols('n')
d=(1+(1/n))**n
result2=limit(d,n,oo)
print(result2)
print(result2.evalf()) #To print the result of the expression after evaluating it, we can use the evalf() method



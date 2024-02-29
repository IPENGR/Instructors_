#sets

'''a={1,2,3,8}
b={3,4}
print(1 in a)
print(4 in a)
print(b.issubset(a))   #checking 'b' is a subset of 'a' or not
'''
#by using functions
def f_issubset(A,B): 
    for e in A: 
        if e in B: 
           pass 
        else:
         return False
    return True
print(f_issubset({1,2,3},{1,2,3,4,5,6}))


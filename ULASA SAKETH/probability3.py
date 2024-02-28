#Calculating Probability over a range

'''Example: Suppose we flip a fair coin 5 times, 
and want to know the probability of getting between 1 and 3 heads.
'''

import scipy.stats as st
prob = st.binom.pmf(1,5,0.5)+st.binom.pmf(2,5,0.5)+st.binom.pmf(3,5,0.5)
print(prob)


#another way
'''
prob = [] 
for 1 in range(1, 4): 
prob. append (st. binom.pmf(1, 5, 0.5))
print (sum(prob)) 
'''

#Example 2: If we want to know the probability of observing 8 or fewer heads from 10 coin flips, 
#we need to add up the values from 0 to 8:

prob = 1 - st.binom.pmf(9, 10, 0.5) 
print (prob) 
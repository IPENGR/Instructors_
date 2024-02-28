#Binomial Distribution
'''random variables can be either discrete or continuous.
 Discrete random variables take on a countable number of distinct values, 
 while continuous random variables can take on any value within a range.
'''

#For example, suppose we flip a fair coin 10 times and count the number of heads. We can use the
#binom.pmf() function to calculate the probability of observing 6 heads as follows:

import scipy.stats as st
n=10
x=6
p=0.5
result1=st.binom.pmf(x,n,p)      #X the value of interest
print(result1)                   #n the number of trials 
                                 #P the probability of success in each trial

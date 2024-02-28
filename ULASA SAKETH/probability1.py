'''
Mathematically, the probability that an event will occur is expressed as a number
between 0 and 1. Nationally, the probabilty of event A is represented by
P(A) .1f P(A) equals 0, event A will almost definitely not occur.
'''
#Random variable
#Example 1 :Let's try to see the outcome of rolling a fair die twice using np. random. choice ()

import numpy as np

die_6 =range(1,7)  
rolling_die = 2 
result=np.random.choice(die_6,size=rolling_die,replace=True)
print(result)

#What could be the outcome if we rolling the die 5 times? 
result_1=np.random.choice(die_6,size=5,replace=True)
print(result_1)

#Example 2: Create a 12 sided die rolling 10 times.
die_12 = range(1,13)
die_rolling = 10
result_2 = np.random.choice(die_12,die_rolling,replace=True)
print(result_2)
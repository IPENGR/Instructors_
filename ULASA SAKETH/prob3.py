# Discrete Probability Distributions
'''Discrete probability distributions describe the probability of 
each possible outcome of a discrete random variable. 
'''

# Importing the binom class from the scipy.stats module
from scipy.stats import binom
# Define parameters for the binomial distribution
n = 5  # Number of trials
p = 0.5  # Probability of success (e.g., getting heads in a coin toss)

# Calculate the Probability Mass Function (PMF) and Cumulative Distribution Function (CDF) 
# for each possible number of successes (k) in the range from 0 to n
pmf_values = binom.pmf(k=range(n+1), n=n, p=p)  # PMF: Probability Mass Function
cdf_values = binom.cdf(k=range(n+1), n=n, p=p)  # CDF: Cumulative Distribution Function

# Print the calculated PMF and CDF values
print("PMF:", pmf_values)
print("CDF:", cdf_values)

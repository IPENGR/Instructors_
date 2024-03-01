#bayes theorem

'''t describes the probability of an event, based on prior knowledge of 
conditions that might be related to the event. 
p(a|b)=p(b|a) x p(a) / p(b) 
'''

# Bayes' Theorem
def bayes_theorem(p_a, p_b_given_a, p_b):
    return (p_b_given_a * p_a) / p_b

# Example usage
p_a = 0.6  # Prior probability of event A
p_b_given_a = 0.7  # Probability of event B given A
p_b = 0.8  # Prior probability of event B
p_a_given_b = bayes_theorem(p_a, p_b_given_a, p_b)
print("Probability of A given B:", p_a_given_b)

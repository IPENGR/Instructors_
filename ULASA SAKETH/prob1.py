'''Probability theory deals with the study of uncertain events.
 It begins with defining a sample space, which is the set of all possible outcomes of an experiment. 
 Events are subsets of the sample space, representing sets of outcomes
'''

sample_space={'H','T'} #Sample space for a coin flip (H for heads, T for tails)

event={'H'} # # Event of getting heads

probability=len(event)/len(sample_space)   # Calculate probability of an event   

print("probability of event :",probability)

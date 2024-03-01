import numpy as np

# Example data
data = np.array([1, 2, 3, 4, 5])

# Probability of each element occurring
probabilities = np.ones_like(data) / len(data)

# Union of events
union = np.union1d(data, [6, 7])

# Intersection of events
intersection = np.intersect1d(data, [3, 4])

# Conditional probability
conditional_prob = probabilities[data == 3]  # Probability of 3 occurring given the data set

print("Data:", data)
print("Probabilities:", probabilities)
print("Union:", union)
print("Intersection:", intersection)
print("Conditional Probability:", conditional_prob)

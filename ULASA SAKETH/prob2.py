# Probability Rules


# Define probabilities
P_A=0.6
P_B=0.3
P_A_and_B=0.2  # # Probability of both events A and B occurring

P_A_or_b=P_A + P_B - P_A_and_B # Calculate probability of A or B using addition rule
print("probability of A or B :",P_A_or_b)

# Calculate conditional probability P(A|B) using multiplication rule
P_A_given_B = P_A_and_B / P_B
print("Conditional probability of A given B:", P_A_given_B)


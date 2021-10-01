from entropy import entropy,relative_entropy
probabilities = [0.01,0.02,0.03,0.02,0.05,0.37,0.02,0.04,0.01,0.39,0.01,0.03]

#Entropy
calculated_entropy = entropy(probabilities)
#Relative entropy
calculated_relative_entropy = relative_entropy(probabilities)
#Redundancy
redundancy = 1 - calculated_relative_entropy
# print(calculated_entropy)
# print(calculated_relative_entropy)
# print(redundancy)
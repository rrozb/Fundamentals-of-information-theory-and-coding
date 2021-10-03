from entropy import entropy,relative_entropy, average
from coding import FannoAlgo
probabilities = [0.01,0.02,0.03,0.02,0.05,0.37,0.02,0.04,0.01,0.39,0.01,0.03]

#Entropy
calculated_entropy = entropy(probabilities)
#Relative entropy
calculated_relative_entropy = relative_entropy(probabilities)
#Redundancy
redundancy = 1 - calculated_relative_entropy
print(calculated_entropy)
print(calculated_relative_entropy)
print(redundancy)

# fanno = {9: '0', 5: '10', 4: '1100', 7: '11010', 2: '11011', 11: '11100', 1: '11101', 3: '111100', 6: '111101', 0: '111110', 8: '1111110', 10: '1111111'}
# huffman = {9: '0', 5: '11', 4: '1000', 7: '10110', 2: '10011', 11: '10100', 1: '101011', 3: '101110', 6: '101111', 0: '100100', 8: '100101', 10: '101010'}
# print(average(probabilities,fanno))
# print(average(probabilities,huffman))
fan = FannoAlgo(probabilities)
fan.run()
print(fan.final_codes)
from entropy import entropy,relative_entropy, average_len
from coding import FannoAlgo,HuffmanAlgo
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

fanno = FannoAlgo(probabilities)
fanno.run()
print(fanno.final_codes)
print('*'*50)
huff = HuffmanAlgo(probabilities)
huff.run()
print(huff.final_codes)

print(average_len(fanno.final_codes))
print(average_len(huff.final_codes))
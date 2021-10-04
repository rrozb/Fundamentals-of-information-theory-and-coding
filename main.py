from entropy import entropy,relative_entropy, average_len,capacity
from coding import FannoAlgo,HuffmanAlgo

probabilities = [0.01,0.02,0.03,0.02,0.05,0.37,0.02,0.04,0.01,0.39,0.01,0.03]

#Entropy
calculated_entropy = entropy(probabilities)
#Relative entropy
calculated_relative_entropy = relative_entropy(probabilities)
#Redundancy
redundancy = 1 - calculated_relative_entropy

print('1. Entropie: ', "{:.4f}".format(calculated_entropy), 'Relativni Entropie:',"{:.4f}".format(calculated_relative_entropy), 'Redundance:',"{:.4f}".format(redundancy))

print('\n2.Fannuv algoritmus:')
fanno = FannoAlgo(probabilities)
fanno.run()
avg_len_fanno = average_len(fanno.final_codes)
print('zpráva   ', 'pravděpodobnost zprávy  ','kód zprávy')
for i,k in fanno.final_codes.items():
    print(f'{i}\t  {k[2]}\t\t\t   {k[0]}')

print('Střední délka: ', avg_len_fanno)
print('\n2.Huffmanuv algoritmus:')
huff = HuffmanAlgo(probabilities)
huff.run()
avg_len_huff = average_len(huff.final_codes)
print('zpráva   ', 'pravděpodobnost zprávy  ','kód zprávy')
for i,k in huff.final_codes.items():
    print(f'{i}\t  {k[2]}\t\t\t   {k[0]}')
print('Střední délka: ', avg_len_huff)

print('\n3.Plati vztah:')
print(f'{calculated_entropy} < {avg_len_huff} < {avg_len_fanno}')

print('\n4.Shannonova veta pro p=0.13:')
proba = 0.13
capacity_of_channel = capacity(proba)
print(f'Kapacita C: {"{:.4f}".format(capacity_of_channel)}')
border = "{:.4f}".format(calculated_entropy / capacity_of_channel)
print(f'Podle Shannonove věty dostáváme hranice n: {border}')
print('tzn. podle prezentaci:')
print('Pro n>= 6 lze přenášet zprávy danneho zdroje dannym kanálem s libovolně malou pravděpodobností chyby pomocí vhodného kódování a dekódování')
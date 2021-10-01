from math import inf
import operator
def fan_alog(probabilities):
    var_dict = {i:k for i,k in enumerate(probabilities)}
    sorted_dict = dict( sorted(var_dict.items(), key=operator.itemgetter(1),reverse=True))
    stack = [sorted_dict]
    codes = {i:'' for i in sorted_dict.keys()}
    while len(stack)>0:
        current_dict= stack[0]
        current_min = inf
        min_i = 0
        x0 = []
        x1 = list(current_dict.values())
        for i,_ in enumerate(current_dict):
            x0.append(x1[0])
            x1.pop(0)
            abs_diff = abs(sum(x0) - sum(x1))
            if abs_diff < current_min:
                current_min = abs_diff
                min_i = i
      
        sliced_dict1 = {k: current_dict[k] for k in list(current_dict.keys())[:min_i+1]}
        sliced_dict2 = {k: current_dict[k] for k in list(current_dict.keys())[min_i+1:]}
        for i in sliced_dict1:
            codes[i] += '0'
        for k in sliced_dict2:
            codes[k] += '1'
        if len(sliced_dict1) >1:
            stack.append(sliced_dict1)
        if len(sliced_dict2) >1:
            stack.append(sliced_dict2)
        stack.pop(0)
    return  codes
probabilities = [0.12, 0.20, 0.11, 0.20, 0.09, 0.09, 0.19]
results = fan_alog(probabilities)
print(results)
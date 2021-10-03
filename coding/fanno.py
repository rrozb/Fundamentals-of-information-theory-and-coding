from math import inf
import operator
from .base import BaseAlgo


class FannoAlgo(BaseAlgo):
    def __init__(self,probabilities):
        super().__init__(probabilities)
        self.stack = [dict( sorted(self.probabilities_dict.items(), key=operator.itemgetter(1),reverse=True))]

    def __update_code(self,sliced_dict1, sliced_dict2):
        '''
        Update final code. 
        '''
        for i in sliced_dict1:
            self.codes[i] += '0'
        for k in sliced_dict2:
            self.codes[k] += '1'
    def __update_stack(self,sliced_dict1, sliced_dict2):
        '''
        Add to stack if it is not a single element.
        '''
        self.stack.pop(0)
        if len(sliced_dict1) >1:
            self.stack.append(sliced_dict1)
        if len(sliced_dict2) >1:
            self.stack.append(sliced_dict2)
    def  run(self):
        while len(self.stack)>0:
            current_dict= self.stack[0]
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
            self.__update_code(sliced_dict1, sliced_dict2)
            self.__update_stack(sliced_dict1, sliced_dict2)

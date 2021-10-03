import operator

class BaseAlgo():
    def __init__(self, probabilities):
        self.probabilities_dict = {i:k for i,k in enumerate(probabilities)}
        self.codes = {i:'' for i in self.probabilities_dict.keys()}
    @property
    def final_codes(self):
        '''
        Return final codes, their length and given probabilities. 
        '''
        return {k: (self.codes[k], len(self.codes[k]), self.probabilities_dict[k]) for k in self.codes}
class Node:
    '''
    Tree node used to build tree for Hufman algorithm.
    '''
    def __init__(self,name, proba, left_branch=None, right_branch=None):
        self.name = name
        self.proba = proba
        self.left_branch = left_branch
        self.right_branch = right_branch
        self.code = ''
import operator

class BaseAlgo():
    def __init__(self, probabilities):
        self.probabilities_dict = {i:k for i,k in enumerate(probabilities)}
        self.codes = {i:'' for i in self.probabilities_dict.keys()}
        # sorted_dict = dict( sorted(var_dict.items(), key=operator.itemgetter(1),reverse=True))

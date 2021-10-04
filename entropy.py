import math
def entropy(probabilities):
    """
    Calculates entropy from given probabilities.
    """
    
    return -sum([x*math.log(x,2) for x in probabilities])

def relative_entropy(probabilities):
    """
    Calculates relative entropy from given probabilities.
    """
    
    return entropy(probabilities)/math.log(len(probabilities), 2)

def average_len(probabilities_dict):
    """
    Calculates average from given dict, its values are tuples such as (code, length of code, probability).
    """
    return sum([code_len*proba for _, code_len,proba in probabilities_dict.values()])

def capacity(proba):
    """
    Calculates capacity from given probability.
    """
    return 1+proba*math.log(proba, 2) + (1-proba)*math.log(1-proba, 2)
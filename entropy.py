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

def average(probabilities, codes):
    """
    Calculates average from given probabilities.
    """
    keylist = list(codes.keys())
    keylist.sort()
    return sum([probabilities[keylist[i]]*len(codes[keylist[i]]) for i in range(len(keylist))])
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
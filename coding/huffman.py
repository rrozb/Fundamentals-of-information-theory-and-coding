# Inspired by https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
from .base import BaseAlgo,Node
class HuffmanAlgo(BaseAlgo):
    def __init__(self,probabilities):
        super().__init__(probabilities)

    
    def __dict2node(self, probabilities_dict):
        nodes = []
        for key,value in probabilities_dict.items():
            nodes.append(Node(key,value))
        return nodes  
    
    def run(self):
        nodes = self.__dict2node(self.probabilities_dict)
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.proba)
            left_node = nodes[0]
            right_node = nodes[1]
            left_node.code = 0
            right_node.code = 1

            newNode = Node(name=(left_node.name+right_node.name), proba= (left_node.proba+right_node.proba), left_branch=left_node, right_branch=right_node)
       
            nodes.remove(left_node)
            nodes.remove(right_node)
            nodes.append(newNode)
        self.__codes_from_nodes(nodes[0])
    def __codes_from_nodes(self, node, val=''):
        newVal = val + str(node.code)
        if(node.left_branch):
            self.__codes_from_nodes(node.left_branch, newVal)
        if(node.right_branch):
            self.__codes_from_nodes(node.right_branch, newVal)
        if(not node.left_branch and not node.right_branch):
            self.codes[node.name] = newVal
        return


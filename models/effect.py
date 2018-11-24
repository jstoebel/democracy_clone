import sys
sys.path.append('.')
from models.node import Node
from models.influence import Influence
class Effect(Node):

    def __init__(self, name, value):
        super().__init__(name, value)
        self.__influences = []

    @property
    def influences(self):
        return self.__influences

    def add_influence(self, influencing_node, weight):
        """
        connect one node as influencing this one.

            :param influencing_node: the node that effects this one
            :param weight: the weight multiplier on this effect.
        """

        influence = Influence(influencing_node, weight)
        self.__influences.append(influence)

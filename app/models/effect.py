from app.models.node import Node
from app.models.influence import Influence

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

    def compute_new_value(self):
        """
        compute new value based on all influences and store it in new_value
        returns nothing
        """

        new_value = self.value
        for i in self.influences:
            new_value += i.influencer.value * i.weight
        self.new_value = new_value

    def flip_value(self):
        self.value = self.new_value
        self.value

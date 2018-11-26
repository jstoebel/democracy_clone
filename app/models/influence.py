class Influence:
    
    def __init__(self, influencer, weight):
        """
        represents the influcene a node has on an effect.
        an Effect instance typically inits an Influence object and stores it in its
        `influences`
            :param self: 
            :param influencer: the node exerting influence on a given node
            :param weight: the weight multiplier the influencer node has the target effect
        """
        self.influencer = influencer
        self.weight = weight
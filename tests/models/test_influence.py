import sys
sys.path.append('.')
from models.influence import Influence
from models.effect import Effect

class TestInfluence:

    def test_init_influ(self):
        e = Effect('spam', .5)
        i = Influence(e, .1)
        assert i.influencer == e 

    def test_init_weight(self):
        e = Effect('spam', .5)
        i = Influence(e, .1)
        assert i.weight == .1
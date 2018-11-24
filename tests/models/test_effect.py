import sys
sys.path.append('.')
from models.effect import Effect

class TestEffect:

    @staticmethod
    def sample_effect(name='spam', value=.5):
        return Effect(name, value)

    def test_init(self):
        assert len(self.sample_effect().influences) == 0

    def test_add_influence(self):
        effect1 = self.sample_effect()
        effect2 = self.sample_effect('second effect', .2)
        effect1.add_influence(effect2, .1)
        assert len(effect1.influences) == 1
        assert effect1.influences[0].influencer == effect2

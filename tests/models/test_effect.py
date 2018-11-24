import sys
sys.path.append('.')
from models.effect import Effect

class TestEffect:

    @staticmethod
    def sample_effect(name='spam', value=.5):
        return Effect(name, value)

    def connected_effect(self):
        """
        creates two effects with the second inflencing the first.
        Returns both as a tuple
        """
        effect1 = self.sample_effect()
        effect2 = self.sample_effect('second effect', .2)
        effect1.add_influence(effect2, .1)
        return (effect1, effect2)

    def test_init(self):
        assert len(self.sample_effect().influences) == 0

    def test_add_influence(self):
        (effect1, effect2) = self.connected_effect()
        assert len(effect1.influences) == 1
        assert effect1.influences[0].influencer == effect2

    def test_compute_new_value(self):
        (effect1, effect2) = self.connected_effect()
        assert effect1.new_value == 5
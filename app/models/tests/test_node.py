from app.models.node import Node

class TestNode:

    @staticmethod
    def sample_node():
        return Node('spam', .5)

    # tests for __init__
    def test_stores_name(self):
        assert self.sample_node().name == 'spam'

    def test_stores_value(self):
        assert self.sample_node().value == .5
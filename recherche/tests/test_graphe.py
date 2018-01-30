from unittest import TestCase

from graphe import Graphe


class TestGraphe(TestCase):

    def setUp(self):

        #    c
        #   /
        #  a
        #   \
        #    d - b
        self.g = Graphe(['a', 'b', 'c', 'd'], [('a', 'c', 1), ('a', 'd', 1), ('b', 'd', 1)])

    def test_voisins(self):
        self.assertEqual(sorted(self.g.voisins('a')), sorted([('c', 1), ('d', 1)]))
        self.assertEqual(sorted(self.g.voisins('d')), sorted([('a', 1), ('b', 1)]))

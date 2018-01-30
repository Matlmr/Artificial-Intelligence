from unittest import TestCase
from math import sqrt

from noeud import Noeud


class TestNoeud(TestCase):

    def test_distance(self):
        n1 = Noeud(0, 0, "1")
        n2 = Noeud(0, 1, "2")
        n3 = Noeud(1, 0, "3")
        n4 = Noeud(1, 1, "4")

        self.assertEqual(n1.distance(n2), 1)
        self.assertEqual(n1.distance(n3), 1)
        self.assertEqual(n1.distance(n4), sqrt(2))

    def test_eq(self):
        n1 = Noeud(1, 2, "blah")
        n2 = Noeud(1, 2, "blah")
        n3 = Noeud(1, 2, "lah")
        n4 = Noeud(1, 3, "blah")
        n5 = Noeud(2, 2, "blah")
        n6 = Noeud(2, 3, "lah")

        self.assertEqual(n1, n2)
        self.assertFalse(n1 == n3)
        self.assertFalse(n1 == n4)
        self.assertFalse(n1 == n5)
        self.assertFalse(n1 == n6)

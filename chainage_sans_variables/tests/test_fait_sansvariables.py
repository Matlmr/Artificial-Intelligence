from unittest import TestCase

from moteurs.sansvariables import Fait


class TestFait(TestCase):

    def setUp(self):
        self.f = Fait('fact1')

    def test_egalite(self):
        f2 = Fait('fact1')
        f3 = Fait('fact3')

        self.assertTrue(f2 == self.f)
        self.assertFalse(f3 == self.f)
        self.assertTrue(f3 != self.f)

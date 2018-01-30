from unittest import TestCase

from moteurs.variables import Fait


class TestFait(TestCase):

    def setUp(self):
        self.f = Fait('fact1')

    def test_egalite(self):
        f2 = Fait('fact1')
        f3 = Fait('fact3')

        f4 = Fait(['a', 'b'])
        f5 = Fait(['a', 'b'])

        self.assertTrue(f2 == self.f)
        self.assertFalse(f3 == self.f)
        self.assertTrue(f3 != self.f)

        self.assertTrue(f4 == f5)

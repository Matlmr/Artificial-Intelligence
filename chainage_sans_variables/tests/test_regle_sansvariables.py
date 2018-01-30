from unittest import TestCase

from moteurs.sansvariables import Regle, Fait

class TestRegle(TestCase):

    def setUp(self):
        self.r = Regle([Fait('fact1'), Fait('fact2')], Fait('conclusion'))

    def test_satisfait_par(self):
        self.assertTrue(self.r.satisfaite_par(Fait('fact1')))
        self.assertFalse(self.r.satisfaite_par(Fait('fact234')))

    #def test_repr(self):
    #    self.assertRegex(self.r.__repr__(), '\[fact., fact.\] => conclusion')

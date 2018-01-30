from unittest import TestCase

from moteurs.variables import Regle, Fait

class TestRegle(TestCase):

    def setUp(self):
        self.r = Regle([Fait(['?x', 'vole'])], Fait(['?x', 'est un oiseau']))
        self.r2 = Regle([Fait(['a', '?y']), Fait(['?x'])], Fait(['?x', '?y']))

    def test_satisfaits_par(self):
        self.assertEqual(self.r.satisfaite_par(Fait(['Titi', 'vole'])), [{'?x': 'Titi'}])
        self.assertFalse(self.r.satisfaite_par(Fait(['Titi', 'ne vole pas'])))

        self.assertEqual(self.r2.satisfaite_par(Fait(['b'])), [{'?x': 'b'}])

    def test_satisfaite(self):
        faits = [Fait(['Titi', 'vole'])]
        self.assertEqual(self.r.satisfaite(faits, {}), [{'?x': 'Titi'}])

        faits = [Fait(['a', 'c']), Fait(['b'])]
        self.assertTrue({'?x': 'b', '?y': 'c'} in self.r2.satisfaite(faits, {'?y': 'c'}))
        self.assertFalse(self.r2.satisfaite(faits, {'?y': 'b'}))

        self.assertFalse(self.r2.satisfaite([Fait(['a', 'c'])], {'?x': 'c'}))

    #def test_repr(self):
    #    self.assertRegex(self.r.__repr__(), '\[fact., fact.\] => conclusion')

__author__ = 'Clement Humbert'
__date__ = '19.02.2015'

from unittest import TestCase

from moteurs.variables.unifieur import Unifieur
from moteurs.variables.exceptions import MatchingException


class TestUnifieur(TestCase):

    def test_unifie_simple(self):
        prop1 = ['?x', 'is', '?y']
        prop2 = ['The night', 'is', 'dark']

        self.assertEqual(Unifieur.unifie(prop2, prop1), {'?x': 'The night', '?y': 'dark'})

        self.assertEqual(Unifieur.unifie(['?x', 'est un', 'doctorant'],
                                         ['vincent', 'est un', 'doctorant']),
                                         {'?x': 'vincent'})
        self.assertEqual(Unifieur.unifie(['vincent', 'est un', 'doctorant'],
                                         ['?x', 'est un', 'doctorant']),
                                         {'?x': 'vincent'})
        self.assertEqual(Unifieur.unifie(['vincent', 'est un', 'doctorant'],
                                         ['vincent', 'est un', 'doctorant']),
                                         {})
        self.assertEqual(Unifieur.unifie(['vincent', 'est un', '?y'],
                                         ['?x', 'est un', 'doctorant']),
                                         {'?x': 'vincent', '?y': 'doctorant'})

        self.assertRaises(MatchingException, Unifieur.unifie,
                          ['vincent', 'est un', 'doctorant'],
                          ['michael', 'est un', 'doctorant'])


    def test_unifie_nested(self):
        prop1 = ['foo', 'jean', ['marc', 'bar', 'paul']]
        prop2 = ['foo', '?x', ['?y', 'bar', '?z']]

        self.assertEqual(Unifieur.unifie(prop1, prop2), {'?x': 'jean', '?y': 'marc', '?z': 'paul'})

        self.assertEqual(Unifieur.unifie(['foo', '?x', ['?y', 'bar', 'jean']],
                                         ['foo', 'jean', ['marc', 'bar', '?z']]),
                                         {'?x': 'jean', '?y': 'marc', '?z': 'jean'})

        self.assertEqual(Unifieur.unifie(['foo', '?x', ['?y', 'bar', 'jean']],
                                         ['foo', 'jean', ['marc', 'bar', '?x']]),
                                         {'?x': 'jean', '?y': 'marc'})
        self.assertRaises(MatchingException, Unifieur.unifie, ['foo', '?x', ['?y', 'bar', 'marc']],
                          ['foo', 'jean', ['marc', 'bar', '?x']])

        self.assertEqual(Unifieur.unifie(['p', '?x', ['f', '?y']],
                                         ['p', ['f', 'a'], '?x']),
                                         {'?x': ['f', 'a'], '?y': 'a'})

    def test_unifie_variables_deux_cotes(self):
        prop1 = ['vincent', 'est un', '?x']
        prop2 = ['?x', 'est un', 'vincent']

        self.assertEqual(Unifieur.unifie(prop1, prop2), {'?x': 'vincent'})

    def test_unifie_unmatchable(self):
        prop1 = ['?x', 'is', '?x']
        prop2 = ['The night', 'is', 'dark']

        self.assertRaises(MatchingException, Unifieur.unifie, prop2, prop1)

    def test_unifie_prop2_too_short(self):
        prop1 = ['?x', 'is', '?y']
        prop2 = ['The night', 'is']

        self.assertRaises(MatchingException, Unifieur.unifie, prop2, prop1)

__author__ = 'Clement Humbert'
__date__ = '19.02.2015'

from unittest import TestCase

from moteurs.variables.filtre import Filtre
from moteurs.variables.exceptions import MatchingException


class TestFiltre(TestCase):

    def test_est_atomique(self):
        self.assertTrue(Filtre.est_atomique('atom'))
        self.assertFalse(Filtre.est_atomique(['not an atom']))

    def test_est_variable(self):
        self.assertTrue(Filtre.est_variable('?x'))
        self.assertFalse(Filtre.est_variable('x'))
        self.assertFalse(Filtre.est_variable(['?x']))

    def test_substitue(self):
        pattern = ['?y', 'is', '?x']
        substitutions = {'?x': 'unknown'}
        self.assertEqual(Filtre.substitue(pattern, substitutions), ['?y', 'is', 'unknown'])

    def test_substitue_single_elements(self):
        self.assertEqual(Filtre.substitue('?x', {'?x': 'unknown'}), 'unknown')

    def test_substitue_recursif(self):
        pattern = ['?y', 'et', ['?x']]
        substitutions = {'?x': 'Dupont', '?y': 'Dupond'}

        self.assertEqual(Filtre.substitue(pattern, substitutions), ['Dupond', 'et', ['Dupont']])

    def test_filtre_simple(self):
        pattern = ['?x', 'is', '?y']
        datum = ['The night', 'is', 'dark']

        self.assertEqual(Filtre.filtre(datum, pattern), {'?x': 'The night', '?y': 'dark'})

        self.assertEqual(Filtre.filtre(['vincent', 'est un', 'doctorant'],
                                       ['vincent', 'est un', 'doctorant']),
                                       {})

        self.assertEqual(Filtre.filtre('vincent', '?x'), {'?x': 'vincent'})

        self.assertEqual(Filtre.filtre(['vincent', 'est un', ['vincent', 'est un', 'doctorant']],
                                       ['vincent', 'est un', ['vincent', 'est un', 'doctorant']]),
                                       {})


        self.assertEqual(Filtre.filtre(['vincent', 'est un', 'doctorant', 'paolo', 'est un', 'doctorant'],
                                       ['?x', 'est un', '?y', '?z', 'est un', '?v']),
                                       {'?x': 'vincent', '?y': 'doctorant', '?z': 'paolo', '?v': 'doctorant'})

        self.assertEqual(Filtre.filtre(['vincent', 'est un', 'vincent'],
                                       ['?x', 'est un', '?x']),
                                       {'?x': 'vincent'})
    def test_filtre_nested(self):
        pattern = ['foo', 'jean', ['marc', 'bar', 'paul']]
        datum = ['foo', '?x', ['?y', 'bar', '?z']]

        self.assertEqual(Filtre.filtre(pattern, datum), {'?x': 'jean', '?y': 'marc', '?z': 'paul'})

    def test_filtre_unmatchable(self):
        pattern = ['?x', 'is', '?x']
        datum = ['The night', 'is', 'dark']

        self.assertRaises(MatchingException, Filtre.filtre, datum, pattern)

        self.assertRaises(MatchingException, Filtre.filtre, ['vincent', 'est un', 'doctorant'],
                          ['paolo', 'est un', 'doctorant'])

        self.assertRaises(MatchingException, Filtre.filtre, ['vincent', 'est un', 'doctorant'],
                          ['vincent', 'est un', ['vincent', 'est un', 'doctorant']])

        self.assertRaises(MatchingException, Filtre.filtre, ['vincent', 'est un', 'doctorant'],
                          ['?x', 'est un', '?x'])

    def test_filtre_datum_too_short(self):
        pattern = ['?x', 'is', '?y']
        datum = ['The night', 'is']

        self.assertRaises(MatchingException, Filtre.filtre, datum, pattern)
